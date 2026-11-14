"""Offline reads from exact-revision Git object stores."""
from pathlib import Path, PurePosixPath
import os
import subprocess
import re
import tempfile
from collections import OrderedDict

_blob_cache=OrderedDict()
_blob_bytes=0
HISTORY_MAX_OBJECTS=4096
HISTORY_MAX_BYTES=2*1024**3
HISTORY_BATCH_SIZE=64


class GitSource:
    def __init__(self, directory, url):
        directory=Path(directory)
        if not directory.is_absolute():directory=Path(__file__).resolve().parents[2]/directory
        self.directory, self.url = directory, url.rstrip("/").removesuffix(".git")
        self.history_fetch_counts={'objects':0,'bytes':0,'batches':0}
        self._history_blob_candidates=None

    def git(self, *args, binary=False, input_text=None):
        try:
            return subprocess.check_output(
                ["git", "-C", str(self.directory), *args], stderr=subprocess.PIPE,
                env={**os.environ, "GIT_NO_LAZY_FETCH": "1"}, text=not binary,
                input=input_text,
            )
        except subprocess.CalledProcessError as exc:
            from .network import log
            error = exc.stderr.decode(errors="replace") if isinstance(exc.stderr,bytes) else exc.stderr
            log(f"Offline Git read failed (exit {exc.returncode}): `{args}` in `{self.directory.name}`. {str(error).strip()[-700:]}")
            raise

    def read(self, commit, path):
        cache = getattr(self, "_text_cache", {})
        key = commit, path
        if key not in cache:
            cache[key] = self.git("show", f"{commit}:{path}")
            self._text_cache = cache
        return cache[key]

    def blob(self,commit,path):
        global _blob_bytes
        key=self.git('rev-parse',f'{commit}:{path}').strip()
        if key in _blob_cache:
            _blob_cache.move_to_end(key)
            return _blob_cache[key]
        value=self.git('show',f'{commit}:{path}',binary=True)
        if len(value)<64*1024**2:
            while _blob_cache and _blob_bytes+len(value)>128*1024**2:
                _,old=_blob_cache.popitem(last=False);_blob_bytes-=len(old)
            _blob_cache[key]=value;_blob_bytes+=len(value)
        return value

    def ensure_revision(self, revision, allow_fetch=False):
        try:
            return self.git('rev-parse','--verify',revision+'^{commit}').strip()
        except subprocess.CalledProcessError:
            if not allow_fetch:
                raise
        from .network import fetch_revision
        fetch_revision(self.directory,revision)
        self._history_blob_candidates=None
        return self.git('rev-parse','--verify',revision+'^{commit}').strip()

    def _metadata_lines(self, *args):
        # Stream tree metadata: large upstream histories need not fit in memory.
        with tempfile.TemporaryFile(dir=self.directory, mode='w+t') as errors:
            command=['git','-C',str(self.directory),*args]
            with subprocess.Popen(command,stdout=subprocess.PIPE,stderr=errors,text=True,
                                  env={**os.environ,'GIT_NO_LAZY_FETCH':'1'}) as process:
                yield from process.stdout
                returncode=process.wait()
            if returncode:
                errors.seek(0)
                message=errors.read()
                from .network import log
                log(f'Offline history metadata read failed (exit {returncode}): {message[-700:]}')
                raise subprocess.CalledProcessError(returncode,command,stderr=message)

    def _history_missing_batch(self, path, missing, partial_output):
        # Rename discovery can read blobs from commits outside the followed
        # path's changes. Index missing versions of each file using tree-only
        # metadata, then fetch those related versions together.
        if self._history_blob_candidates is None:
            absent={line[1:].strip() for line in self._metadata_lines(
                'rev-list','--objects','--all','--missing=print') if line.startswith('?')}
            by_path={};by_object={};by_directory={}
            for line in self._metadata_lines('log','--all','--root','-m','--raw','--no-abbrev',
                                             '--no-renames','--format='):
                if not line.startswith(':') or '\t' not in line:
                    continue
                raw,filename=line.rstrip('\n').split('\t',1)
                fields=raw.split()
                for mode,oid in zip((fields[0][1:],fields[1]),fields[2:4]):
                    if mode in ('100644','100755','120000') and oid in absent:
                        by_path.setdefault(filename,set()).add(oid)
                        by_object.setdefault(oid,set()).add(filename)
                        by_directory.setdefault(str(PurePosixPath(filename).parent),set()).add(oid)
            self._history_blob_candidates=(by_path,by_object,by_directory)
        by_path,by_object,by_directory=self._history_blob_candidates
        paths={path}|by_object.get(missing,set())
        for line in partial_output.splitlines():
            if line.startswith('R100\t'):
                paths.update(line.split('\t')[1:])
        versions=[oid for p in sorted(paths) for oid in sorted(by_path.get(p,()))]
        peers=[oid for p in sorted(paths) for oid in sorted(by_directory.get(str(PurePosixPath(p).parent),()))]
        candidates=list(dict.fromkeys([missing]+versions+peers))
        available=self.git('cat-file','--batch-check=%(objectname) %(objecttype)',input_text='\n'.join(candidates)+'\n')
        return [line.split()[0] for line in available.splitlines() if line.endswith(' missing')][:HISTORY_BATCH_SIZE]

    def history(self, path,allow_fetch=False):
        # Keep exact-content rename semantics. Git can still inspect unrelated
        # blobs during this traversal, so recover them within explicit budgets.
        fetched=set()
        history_warning=None
        from .network import fetch_objects,object_store_bytes,log
        while True:
            try:
                output=self.git('log','--all','--follow','--find-renames=100%',
                                '--format=@@@%H|%ct|%cI|%s','--name-status','--',path)
                break
            except subprocess.CalledProcessError as exc:
                message=exc.stderr.decode(errors='replace') if isinstance(exc.stderr,bytes) else exc.stderr or ''
                missing=re.search(r'could not fetch ([0-9a-f]{40})',message)
                reason='offline or unavailable object'
                if allow_fetch and missing and missing.group(1) not in fetched:
                    counts=self.history_fetch_counts
                    remaining_objects=HISTORY_MAX_OBJECTS-counts['objects']
                    remaining_bytes=HISTORY_MAX_BYTES-counts['bytes']
                    reason='history object/byte cap reached'
                    if remaining_objects>0 and remaining_bytes>131072:
                        try:
                            batch=self._history_missing_batch(path,missing.group(1),exc.output or '')[:remaining_objects]
                            if not batch:
                                raise ValueError('No missing rename candidate objects could be identified')
                            before=object_store_bytes(self.directory)
                            counts['objects']+=len(batch)
                            counts['batches']+=1
                            fetched.update(batch)
                            try:
                                # Leave room for pack indexes and fetch metadata.
                                fetch_objects(self.directory,batch,max_pack_bytes=remaining_bytes-65536-len(batch)*64)
                            finally:
                                counts['bytes']+=max(0,object_store_bytes(self.directory)-before)
                                log(f'History fetch counts for {self.url}: {counts["objects"]} objects requested, '
                                    f'{counts["bytes"]} stored object bytes, {counts["batches"]} batches; '
                                    f'caps {HISTORY_MAX_OBJECTS} objects / {HISTORY_MAX_BYTES} bytes.')
                            if counts['bytes']<=HISTORY_MAX_BYTES:
                                continue
                        except (RuntimeError,ValueError,OSError,subprocess.SubprocessError) as fetch_error:
                            reason=f'bounded history fetch stopped: {fetch_error}'
                history_warning=('Exact-rename traversal required unavailable unrelated blobs; current-path history was inspected, '
                                 'older renamed paths remain unresolved; '+reason)
                log(f'History coverage warning for {self.url} {path}: {history_warning}')
                output=self.git('log','--all','--no-renames','--format=@@@%H|%ct|%cI|%s','--name-status','--',path)
                break
        rows=[];current_path=path;row=None
        for line in output.splitlines():
            if line.startswith('@@@'):
                row=dict(zip(('commit','timestamp','date','subject'),line[3:].split('|',3)))
                row['file']=current_path
                rows.append(row)
            elif row is not None and line.startswith('R100\t'):
                _,old,new=line.split('\t',2)
                row['file']=new
                row['rename_from']=old
                current_path=old
            elif row is not None and '\t' in line:
                status,actual=line.split('\t',1)
                if actual==current_path:
                    row['file']=actual
                    row['deleted']=status=='D'
        if history_warning:
            for row in rows:row['history_incomplete']=history_warning
        return rows

    def permalink(self, commit, path, line):
        return f"{self.url}/blob/{commit}/{path}#L{line}"

    def history_for_paths(self,paths):
        output=self.git('log','--all','--no-renames','--format=%H|%ct|%cI|%s','--',*sorted(set(paths)))
        return [dict(zip(('commit','timestamp','date','subject'),line.split('|',3))) for line in output.splitlines()]

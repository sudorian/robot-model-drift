"""Offline reads from exact-revision Git object stores."""
from pathlib import Path
import os
import subprocess
import re
from collections import OrderedDict

_blob_cache=OrderedDict()
_blob_bytes=0


class GitSource:
    def __init__(self, directory, url):
        directory=Path(directory)
        if not directory.is_absolute():directory=Path(__file__).resolve().parents[2]/directory
        self.directory, self.url = directory, url.rstrip("/").removesuffix(".git")

    def git(self, *args, binary=False):
        try:
            return subprocess.check_output(
                ["git", "-C", str(self.directory), *args], stderr=subprocess.PIPE,
                env={**os.environ, "GIT_NO_LAZY_FETCH": "1"}, text=not binary,
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

    def history(self, path,allow_fetch=False):
        # Exact-content renames can be followed using object IDs without fetching
        # unrelated geometry blobs for heuristic similarity analysis.
        fetched=set()
        history_warning=None
        for attempt in range(6):
            try:
                output=self.git('log','--all','--follow','--find-renames=100%',
                                '--format=@@@%H|%ct|%cI|%s','--name-status','--',path)
                break
            except subprocess.CalledProcessError as exc:
                message=exc.stderr.decode(errors='replace') if isinstance(exc.stderr,bytes) else exc.stderr or ''
                missing=re.search(r'could not fetch ([0-9a-f]{40})',message)
                if not allow_fetch or not missing or missing.group(1) in fetched or attempt==5:
                    history_warning='Exact-rename traversal required unavailable unrelated blobs; current-path history was inspected, older renamed paths remain unresolved'
                    from .network import log
                    log(f'History coverage warning for {self.url} {path}: {history_warning}')
                    output=self.git('log','--all','--no-renames','--format=@@@%H|%ct|%cI|%s','--name-status','--',path)
                    break
                from .network import fetch_objects
                fetched.add(missing.group(1));fetch_objects(self.directory,[missing.group(1)])
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

"""Explicit, logged Git-only source acquisition with a hard workspace budget."""
from pathlib import Path
import datetime
import os
import shlex
import shutil
import subprocess
from .publication import public_text


ROOT = Path(__file__).resolve().parents[2]


def log(message):
    with (ROOT / "NOTES.md").open("a") as file:
        file.write("\n- " + public_text(message, ROOT).replace("\x00", "").rstrip() + "\n")


def disk_bytes():
    # du counts allocated filesystem blocks, including ignored clones and env.
    return int(subprocess.check_output(["du", "-sk", str(ROOT)], text=True).split()[0]) * 1024


def network_git(args, purpose, input_text=None):
    if not any(x in args for x in ("clone", "fetch")):
        raise ValueError("Only Git clone/fetch network operations are authorized")
    for value in args:
        if "://" in value and not value.startswith("https://github.com/"):
            raise ValueError("Network URL is outside github.com")
    used = disk_bytes()
    if used >= 12_000_000_000 or shutil.disk_usage(ROOT).free < 3_000_000_000:
        raise RuntimeError("Disk guard stopped network acquisition before the 15 GB cap")
    command = ["git", "-c", "pack.threads=1", "-c", "index.threads=1", "-c", "fetch.parallel=1", "-c", "gc.auto=0", "-c", "maintenance.auto=false", *args]
    log(f"Network command `{shlex.join(command)}` — {purpose}. Parent process runs at nice 15; lazy fetching disabled.")
    if input_text:
        log(f"Network command stdin object IDs: `{input_text.strip().replace(chr(10),' ')}`")
    try:
        result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True,
                                input=input_text, env={**os.environ, "GIT_NO_LAZY_FETCH": "1"}, timeout=600)
    except subprocess.TimeoutExpired:
        log("Network command failed: exceeded 600-second timeout; no result inferred.")
        raise
    tail = (result.stdout + result.stderr).strip()[-2500:]
    log(f"Network outcome: exit {result.returncode}. {tail}")
    if disk_bytes() >= 15_000_000_000:
        raise RuntimeError("Workspace exceeded disk guard; stop immediately")
    if result.returncode:
        raise RuntimeError(f"Git network command failed ({result.returncode}): {tail}")


def clone_repo(url, directory, limit="100k"):
    path = ROOT / directory
    path.parent.mkdir(parents=True,exist_ok=True)
    if not (path / ".git").is_dir():
        network_git(["clone", "--filter=blob:none", "--no-checkout", url + ".git", str(path)],
                    "retrieve source commit/tree history without model blobs")
        fetch_blobs(path,limit)
    return path


def refresh_repo(source):
    """Refresh the cached default branch through an explicit logged fetch."""
    remote=source.git('remote','get-url','origin').strip()
    if not remote.startswith('https://github.com/'):
        raise ValueError('Refusing source refresh outside github.com')
    network_git(['-C',str(source.directory),'fetch','--filter=blob:none','--no-tags','origin',
                 'HEAD','+refs/heads/*:refs/remotes/origin/*'],
                'refresh the upstream branch tips before selecting latest H')
    sha=source.git('rev-parse','FETCH_HEAD^{commit}').strip()
    source.git('update-ref','HEAD',sha)
    return sha


def fetch_blobs(directory, limit="20m", ref="HEAD"):
    network_git(["-C", str(directory), "fetch", "--no-tags", "--refetch", f"--filter=blob:limit={limit}", "origin", ref],
                f"retrieve omitted source/mesh blobs below {limit} for CPU compilation")


def fetch_objects(directory,objects):
    for oid in objects:
        if not __import__('re').fullmatch(r'[0-9a-f]{40}',oid):
            raise ValueError('Invalid Git object ID')
    network_git(['-C',str(directory),'-c','fetch.negotiationAlgorithm=noop','fetch','origin','--no-tags',
                 '--no-write-fetch-head','--recurse-submodules=no','--filter=blob:none','--stdin'],
                'retrieve only specifically required source/resource blobs using the promisor-fetch protocol',
                '\n'.join(objects)+'\n')


def ensure_menagerie_texts(source,commit,allow_network=False):
    rows=source.git('ls-tree','-r',commit).splitlines()
    ids=[]
    for row in rows:
        metadata,path=row.split('\t',1)
        if not path.startswith('test/') and (path.endswith('.xml') or path.endswith('/README.md') or path.endswith('/CHANGELOG.md')):
            ids.append(metadata.split()[2])
    result=subprocess.run(['git','-C',str(source.directory),'cat-file','--batch-check=%(objectname) %(objecttype)'],
                          input='\n'.join(ids)+'\n',capture_output=True,text=True,
                          env={**os.environ,'GIT_NO_LAZY_FETCH':'1'},check=True)
    missing=sorted(set(line.split()[0] for line in result.stdout.splitlines() if line.endswith(' missing')))
    if missing:
        if not allow_network:
            raise ValueError(f'{len(missing)} required Menagerie text blobs are absent; rerun with --fetch')
        fetch_objects(source.directory,missing)
    return len(missing)

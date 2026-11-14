from pathlib import Path
import pytest
from drift.network import refresh_repo
import subprocess
import sys


class Source:
    directory=Path('.cache/synthetic')
    def __init__(self,remote):
        self.remote=remote
        self.calls=[]
    def git(self,*args):
        self.calls.append(args)
        if args==('remote','get-url','origin'):return self.remote
        if args==('rev-parse','FETCH_HEAD^{commit}'):return 'a'*40
        if args[:2]==('update-ref','HEAD'):return ''
        raise AssertionError(args)


def test_refresh_uses_remote_default_head_and_logged_fetch(monkeypatch):
    calls=[]
    monkeypatch.setattr('drift.network.network_git',lambda *a:calls.append(a))
    source=Source('https://github.com/synthetic/test.git')
    assert refresh_repo(source)=='a'*40
    assert calls[0][0][-2:]==['HEAD','+refs/heads/*:refs/remotes/origin/*']
    assert source.calls[-1]==('update-ref','HEAD','a'*40)


def test_refresh_refuses_an_unapproved_network_host(monkeypatch):
    monkeypatch.setattr('drift.network.network_git',lambda *a:pytest.fail('network must not run'))
    with pytest.raises(ValueError,match='outside github.com'):
        refresh_repo(Source('https://example.org/unapproved.git'))


def test_fetch_pack_limit_is_enforced_before_file_growth(tmp_path):
    from drift.network import _file_size_limit
    destination=tmp_path/'oversized-pack'
    result=subprocess.run([sys.executable,'-c',
        'import sys; f=open(sys.argv[1],"wb"); f.write(b"x"*8192); f.flush(); f.close()',str(destination)],
        preexec_fn=lambda:_file_size_limit(4096),capture_output=True)
    assert result.returncode!=0
    assert destination.stat().st_size<=4096


def test_pin_fetch_records_a_full_sha_without_changing_default_head(monkeypatch):
    from drift.network import fetch_revision
    calls=[]
    monkeypatch.setattr('drift.network.network_git',lambda *args,**kwargs:calls.append((args,kwargs)))
    oid='a'*40
    fetch_revision(Path('.cache/test'),oid)
    assert calls[0][0][0][-1]==oid+':refs/drift/pins/'+oid
    assert '--filter=blob:none' in calls[0][0][0]
    assert calls[0][1]['max_pack_bytes']==128*1024**2
    with pytest.raises(ValueError):fetch_revision(Path('.cache/test'),'short')

from pathlib import Path
import pytest
from drift.network import refresh_repo


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

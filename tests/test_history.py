from drift.sources import GitSource
import subprocess
import pytest


def test_exact_rename_history_tracks_each_revision_path():
    source=GitSource('.cache/test','https://github.com/synthetic/test')
    source.git=lambda *args:'@@@new|20|date2|rename\n\nR100\told.urdf\tnew.urdf\n@@@old|10|date1|initial\n\nA\told.urdf\n'
    rows=source.history('new.urdf')
    assert rows[0]['file']=='new.urdf'
    assert rows[1]['file']=='old.urdf'


def test_batches_continue_beyond_five_retries(monkeypatch):
    source=GitSource('.cache/test','https://github.com/synthetic/test')
    ids=[f'{i:040x}' for i in range(1,15)]
    fetched=set();calls=[];messages=[]
    def git(*args,**kwargs):
        remaining=[oid for oid in ids if oid not in fetched]
        if remaining:
            raise subprocess.CalledProcessError(128,args,output='',stderr='could not fetch '+remaining[0])
        return '@@@new|20|date|initial\nA\trobot.xml\n'
    source.git=git
    source._history_missing_batch=lambda *args:[oid for oid in ids if oid not in fetched][:2]
    def fetch(directory,batch,max_pack_bytes=None):
        assert max_pack_bytes>0
        calls.append(batch);fetched.update(batch)
    monkeypatch.setattr('drift.network.fetch_objects',fetch)
    monkeypatch.setattr('drift.network.object_store_bytes',lambda _:len(fetched)*100)
    monkeypatch.setattr('drift.network.log',messages.append)
    rows=source.history('robot.xml',allow_fetch=True)
    assert len(calls)==7 and all(len(batch)==2 for batch in calls)
    assert not any(r.get('history_incomplete') for r in rows)
    assert source.history_fetch_counts=={'objects':14,'bytes':1400,'batches':7}
    assert '14 objects requested' in messages[-1]


@pytest.mark.parametrize('stop', ['offline','object_cap','byte_cap','fetch_failure','repeat'])
def test_unavailable_history_keeps_honest_fallback(monkeypatch,stop):
    source=GitSource('.cache/test','https://github.com/synthetic/test')
    oid='a'*40;fetched=[];messages=[]
    def git(*args,**kwargs):
        if '--no-renames' in args:
            return '@@@new|20|date|initial\nA\trobot.xml\n'
        raise subprocess.CalledProcessError(128,args,output='',stderr='could not fetch '+oid)
    source.git=git
    source._history_missing_batch=lambda *args:[oid]
    def fetch(*args,**kwargs):
        fetched.append(args)
        if stop=='fetch_failure':raise RuntimeError('pack byte ceiling reached')
    monkeypatch.setattr('drift.network.fetch_objects',fetch)
    monkeypatch.setattr('drift.network.object_store_bytes',lambda _:0)
    monkeypatch.setattr('drift.network.log',messages.append)
    if stop=='object_cap':monkeypatch.setattr('drift.sources.HISTORY_MAX_OBJECTS',0)
    if stop=='byte_cap':monkeypatch.setattr('drift.sources.HISTORY_MAX_BYTES',131072)
    rows=source.history('robot.xml',allow_fetch=stop!='offline')
    assert rows[0]['history_incomplete']
    assert len(fetched)==int(stop in ('fetch_failure','repeat'))
    assert 'History coverage warning' in messages[-1]


def test_batch_index_finds_unrelated_missing_file_versions(monkeypatch):
    source=GitSource('.cache/test','https://github.com/synthetic/test')
    ids=[f'{i:040x}' for i in range(1,5)]
    calls=[]
    def metadata(*args):
        calls.append(args)
        if args[0]=='rev-list':return iter('?'+oid+'\n' for oid in ids)
        return iter([f':100644 100644 {ids[0]} {ids[1]} M\tLICENSE\n',
                     f':100644 100644 {ids[2]} {ids[3]} M\trobot.xml\n'])
    source._metadata_lines=metadata
    source.git=lambda *args,**kwargs:''.join(oid+' missing\n' for oid in kwargs['input_text'].splitlines())
    assert set(source._history_missing_batch('robot.xml',ids[0],''))==set(ids)
    source._history_missing_batch('robot.xml',ids[0],'')
    assert len(calls)==2  # The repository metadata index is reused.


def test_absent_pinned_commit_is_explicitly_fetched_only_when_allowed(monkeypatch):
    source=GitSource('.cache/test','https://github.com/synthetic/test')
    oid='a'*40;fetched=[]
    def git(*args):
        if not fetched:raise subprocess.CalledProcessError(128,args,stderr='unknown revision')
        return oid+'\n'
    source.git=git
    monkeypatch.setattr('drift.network.fetch_revision',lambda directory,revision:fetched.append(revision))
    with pytest.raises(subprocess.CalledProcessError):source.ensure_revision(oid)
    assert not fetched
    assert source.ensure_revision(oid,allow_fetch=True)==oid
    assert fetched==[oid]


@pytest.mark.parametrize('budget', ['objects','bytes'])
def test_history_budget_is_shared_across_paths_and_checks_before_fetch(monkeypatch,budget):
    source=GitSource('.cache/test','https://github.com/synthetic/test')
    ids=[f'{i:040x}' for i in range(1,10)];fetched=set();calls=[]
    def git(*args,**kwargs):
        if '--no-renames' in args:return '@@@new|20|date|initial\nA\trobot.xml\n'
        oid=next(oid for oid in ids if oid not in fetched)
        raise subprocess.CalledProcessError(128,args,output='',stderr='could not fetch '+oid)
    source.git=git
    source._history_missing_batch=lambda *args:[oid for oid in ids if oid not in fetched][:2]
    def fetch(directory,batch,max_pack_bytes=None):
        calls.append(batch);fetched.update(batch)
    monkeypatch.setattr('drift.network.fetch_objects',fetch)
    monkeypatch.setattr('drift.network.object_store_bytes',lambda _:len(fetched)*100000)
    monkeypatch.setattr('drift.network.log',lambda *args:None)
    monkeypatch.setattr('drift.sources.HISTORY_MAX_OBJECTS',3 if budget=='objects' else 100)
    monkeypatch.setattr('drift.sources.HISTORY_MAX_BYTES',1000000 if budget=='objects' else 300000)
    assert source.history('first.xml',allow_fetch=True)[0]['history_incomplete']
    previous=list(calls)
    assert source.history('second.xml',allow_fetch=True)[0]['history_incomplete']
    assert calls==previous
    assert source.history_fetch_counts['objects']==(3 if budget=='objects' else 2)

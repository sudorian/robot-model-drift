import json
import sys

import pytest

from drift import cli, gate, network, reports, survey


def setup_check(monkeypatch, tmp_path, statuses, extra_args=()):
    (tmp_path / '.cache/menagerie/.git').mkdir(parents=True)
    entries=[{'model': 'synthetic_'+str(i)} for i in range(len(statuses))]
    class Source:
        def __init__(self, *args): pass
        def git(self, *args): return 'a'*40+'\n'
    class Runner:
        def __init__(self, *args): pass
        def check(self, entry, *args):
            status=statuses[int(entry['model'].split('_')[-1])]
            return {'model':entry['model'],'status':status,'source':{'method':'unknown'}}
    monkeypatch.setattr(gate, 'GitSource', Source)
    monkeypatch.setattr(network, 'ensure_menagerie_texts', lambda *args: None)
    monkeypatch.setattr(survey, 'inventory', lambda *args, **kwargs: entries)
    monkeypatch.setattr(survey, 'Runner', Runner)
    monkeypatch.setattr(survey, 'save', lambda *args: None)
    monkeypatch.setattr(reports, 'write_model', lambda *args: None)
    monkeypatch.setattr(sys, 'argv', ['drift','--root',str(tmp_path),'check','all',*extra_args])


@pytest.mark.parametrize('status,expected', [
    ('complete',0), ('incomplete',0), ('partial history',0),
    ('unknown upstream',0), ('error',2),
])
def test_check_exit_status_distinguishes_coverage_from_errors(monkeypatch,tmp_path,capsys,status,expected):
    setup_check(monkeypatch,tmp_path,[status])
    with pytest.raises(SystemExit) as exc:
        cli.main()
    assert exc.value.code==expected
    summary=capsys.readouterr().out.splitlines()[-1]
    assert json.loads(summary.removeprefix('Status counts: '))=={status:1}


def test_full_survey_prints_all_status_counts(monkeypatch,tmp_path,capsys):
    statuses=['complete','partial history','incomplete','unknown upstream','error','complete']
    setup_check(monkeypatch,tmp_path,statuses)
    with pytest.raises(SystemExit) as exc:
        cli.main()
    assert exc.value.code==2
    assert json.loads(capsys.readouterr().out.splitlines()[-1].removeprefix('Status counts: '))=={
        'complete':2,'partial history':1,'incomplete':1,'unknown upstream':1,'error':1}


def test_resumed_survey_includes_saved_statuses(monkeypatch,tmp_path,capsys):
    setup_check(monkeypatch,tmp_path,['error'],['--resume'])
    (tmp_path/'report').mkdir()
    (tmp_path/'report/results.json').write_text(json.dumps([
        {'model':'synthetic_0','status':'error','source':{'method':'unknown'}}]))
    with pytest.raises(SystemExit) as exc:
        cli.main()
    assert exc.value.code==2
    assert 'Status counts: {"error": 1}' in capsys.readouterr().out

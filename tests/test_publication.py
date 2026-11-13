import json
import os
from pathlib import Path
import subprocess

import yaml

from drift.publication import public_data, public_text


def test_paths_with_spaces_and_interpreters_are_portable(tmp_path):
    root = tmp_path / 'workspace with spaces'
    source = root / '.cache' / 'model with spaces.urdf'
    interpreter = tmp_path / 'tools' / 'bin' / 'python3.11'
    assert public_text(str(source), root) == '.cache/model with spaces.urdf'
    assert public_text(f"File '{source}' failed", root) == "File '.cache/model with spaces.urdf' failed"
    assert public_text(str(root), root) == '.'
    assert public_text(str(root / '.venv/bin/python'), root) == '.venv/bin/python'
    assert public_text(str(interpreter), root) == 'python3.11'
    sibling = tmp_path / 'elsewhere' / 'input.urdf'
    assert public_text(str(sibling), root) == os.path.relpath(sibling, root)


def test_source_references_xml_numbers_and_relative_paths_survive(tmp_path):
    source = 'https://github.com/synthetic/robot/blob/' + 'a' * 40 + '/model.urdf#L12'
    data = {'source': source, 'package': 'package://robot/model.urdf',
            'xml': '<robot><link/></robot>', 'relative': '.cache/model.urdf',
            'value': [51.437, 59.33801256637062, None, True, {'class': 'STALE'}],
            str(tmp_path / 'error'): str(tmp_path / 'model.urdf')}
    expected = dict(data)
    expected['error'] = expected.pop(str(tmp_path / 'error')).removeprefix(str(tmp_path) + os.sep)
    cleaned = public_data(data, tmp_path)
    assert cleaned == expected
    assert public_data(cleaned, tmp_path) == cleaned
    assert str(tmp_path / 'error') in data  # Original compiler inputs are untouched.


def test_exception_paths_are_sanitized_at_every_publication_boundary(tmp_path, monkeypatch):
    from drift import network, reports, survey
    for module in (network, reports, survey):
        monkeypatch.setattr(module, 'ROOT', tmp_path)
    (tmp_path / 'report').mkdir()
    (tmp_path / 'provenance').mkdir()
    failure = subprocess.CalledProcessError(128, ['git', '-C', str(tmp_path / '.cache/source'), 'show', 'missing'])
    raw = str(failure)
    result = {'model': 'synthetic', 'status': 'error', 'source': {'method': 'unknown'},
              'reason': raw, 'candidate_errors': [raw],
              'source_candidates': [{'commit': 'a' * 40, 'error': raw}]}
    network.log(raw)
    survey.save([result])
    reports.write_model(result)
    expected = public_text(raw, tmp_path)
    saved = json.loads((tmp_path / 'report/results.json').read_text())[0]
    provenance = yaml.safe_load((tmp_path / 'provenance/synthetic.yaml').read_text())
    assert saved['candidate_errors'] == [expected]
    assert provenance['source_candidates'][0]['error'] == expected
    assert expected in (tmp_path / 'report/synthetic.md').read_text()
    assert expected in (tmp_path / 'NOTES.md').read_text()
    for path in [tmp_path / 'NOTES.md', *tmp_path.glob('report/*'), *tmp_path.glob('provenance/*')]:
        assert str(tmp_path) not in path.read_text(), path.name
    assert result['candidate_errors'] == [raw]

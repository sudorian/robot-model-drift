import json
from pathlib import Path
import pytest


def test_all_surveyed_standalone_models_compare_with_themselves_without_findings():
    path=Path(__file__).resolve().parents[1]/'report/results.json'
    if not path.exists():pytest.skip('Run the full survey first')
    results=json.loads(path.read_text())
    inventory=path.with_name('inventory.json')
    if inventory.exists():
        expected={entry['model'] for entry in json.loads(inventory.read_text())}
        assert {result['model'] for result in results}==expected
    assert results
    for result in results:
        assert result.get('self_comparisons'),result['model']
        for check in result['self_comparisons']:
            assert check['status']=='passed',(result['model'],check)
            assert check['findings']==0,(result['model'],check)


def test_robotiq_comparisons_select_the_full_gripper_not_its_fixed_base_macro():
    path=Path(__file__).resolve().parents[1]/'report/results.json'
    if not path.exists():pytest.skip('Run the full survey first')
    for result in json.loads(path.read_text()):
        if result['model'] in ('robotiq_2f85','robotiq_2f85_v4') and result.get('comparison'):
            snapshot=result['upstream']['snapshot']
            assert len(snapshot['joints'])>=2
            assert any(name.startswith('left_') for name in snapshot['bodies'])
            assert any(name.startswith('right_') for name in snapshot['bodies'])


def test_published_counts_and_exclusions_follow_the_kinematic_guard():
    from collections import Counter
    path=Path(__file__).resolve().parents[1]/'report/results.json'
    if not path.exists():pytest.skip('Run the full survey first')
    for result in json.loads(path.read_text()):
        comparison=result.get('comparison')
        if not comparison:continue
        if 'kinematics' not in comparison:pytest.skip('Rerun the saved survey with the kinematic guard')
        assert comparison['counts']==dict(Counter(r['class'] for r in comparison['findings']))
        if any(not k['com_eligible'] for k in comparison['kinematics'].values()):
            assert all(r['quantity'] not in ('com_registered','total_com_registered') for r in comparison['findings'])
        for row in comparison['excluded_findings']:
            assert row['quantity'] in ('com_registered','total_com_registered')
            assert row['raw_values']['m']==row['m']
            assert row['exclusion_reason']

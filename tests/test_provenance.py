from drift.provenance import select_source, class_with_provenance
from drift.compare import Tolerances


def candidate(time, matches=True):
    return {"timestamp": time, "matches": matches, "commit": str(time)}


def test_newest_dated_match_wins():
    assert select_source([candidate(1), candidate(3), candidate(8)], 5)["candidate"]["timestamp"] == 3


def test_earliest_matching_proxy_only_without_earlier_public_history():
    p = select_source([candidate(8), candidate(6, False), candidate(7)], 5)
    assert p["method"] == "proxy"
    assert p["candidate"]["timestamp"] == 7
    assert class_with_provenance(1, 1, 2, "mass", "proxy", Tolerances()) == "STALE (inferred)"


def test_no_match_never_counts_as_stale():
    p = select_source([candidate(1, False), candidate(8, False)], 5)
    assert p["method"] == "none"
    assert class_with_provenance(1, None, 2, "mass", "none", Tolerances()) == "NO MATCHING SOURCE"


def test_nonmatching_earlier_history_does_not_authorize_proxy():
    assert select_source([candidate(1, False), candidate(8)], 5)["method"] == "unknown"


def test_pinned_has_priority_over_matching():
    pinned = candidate(2, False)
    assert select_source([candidate(1)], 5, pinned)["candidate"] is pinned


def test_failed_history_is_unknown_not_no_match():
    result=select_source([{**candidate(1,False),'error':'unresolved mesh'}],5)
    assert result['method']=='unknown'
    assert result['confidence']=='incomplete'


def test_incomplete_rename_history_cannot_claim_a_proxy_or_no_match():
    result=select_source([{**candidate(8),'history_incomplete':'older path unresolved'}],5)
    assert result['method']=='unknown'


def test_dependency_commit_before_source_exists_is_not_a_public_revision():
    absent={**candidate(1,False),'deleted':True}
    result=select_source([absent,candidate(8)],5)
    assert result['method']=='proxy'
    assert result['candidate']['timestamp']==8

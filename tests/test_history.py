from drift.sources import GitSource


def test_exact_rename_history_tracks_each_revision_path():
    source=GitSource('.cache/test','https://github.com/synthetic/test')
    source.git=lambda *args:'@@@new|20|date2|rename\n\nR100\told.urdf\tnew.urdf\n@@@old|10|date1|initial\n\nA\told.urdf\n'
    rows=source.history('new.urdf')
    assert rows[0]['file']=='new.urdf'
    assert rows[1]['file']=='old.urdf'

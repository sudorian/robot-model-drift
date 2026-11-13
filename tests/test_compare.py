import pytest
from drift.compare import Tolerances, classify


@pytest.mark.parametrize("m,s,h,expected", [
    (1, 1, 1, "unchanged"),
    (1, 1, 2, "STALE"),
    (1, 2, 2, "undocumented derivation difference"),
    (2, 1, 2, "already synced"),
    (1, 2, 3, "needs a human look"),
    (1, None, 2, "unknown"),
])
def test_classes(m, s, h, expected):
    assert classify(m, s, h, "mass") == expected


def test_documented_requires_explicit_evidence():
    assert classify(1, 2, 2, "mass", documented=True) == "documented derivation difference"


def test_tolerance_sensitivity_and_absolute_mass_floor():
    assert Tolerances().close(0, 0.0009, "mass")
    assert not Tolerances(scale=0.5).close(0, 0.0009, "mass")
    assert Tolerances(scale=2).close(0, 0.0019, "mass")
    assert Tolerances().close(100, 100.4, "mass")
    assert not Tolerances(scale=0.5).close(100, 100.4, "mass")


def test_com_is_euclidean_not_per_coordinate():
    assert not Tolerances().close([0, 0, 0], [0.0004, 0.0004, 0], "com")


def test_nonfinite_or_different_shapes_do_not_compare_equal():
    assert not Tolerances().close(float("nan"), float("nan"), "mass")
    assert not Tolerances().close([1, 2], 1, "range")


def test_invalid_tolerance_configuration_rejected():
    with pytest.raises(ValueError):
        Tolerances(scale=-1)

import pytest

from statistics_helpers import clamp, mean, median


def test_mean_of_integers():
    assert mean([1, 2, 3, 4]) == 2.5


def test_mean_rejects_empty_input():
    with pytest.raises(ValueError):
        mean([])


def test_median_odd_length():
    assert median([3, 1, 2]) == 2


def test_median_even_length():
    assert median([4, 1, 3, 2]) == 2.5


def test_median_rejects_empty_input():
    with pytest.raises(ValueError):
        median([])


def test_clamp_within_range():
    assert clamp(5, 0, 10) == 5


def test_clamp_below_lower_bound():
    assert clamp(-3, 0, 10) == 0


def test_clamp_above_upper_bound():
    assert clamp(42, 0, 10) == 10


def test_clamp_rejects_inverted_bounds():
    with pytest.raises(ValueError):
        clamp(1, 10, 0)

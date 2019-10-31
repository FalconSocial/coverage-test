"""Test helper functions."""
import pytest

from app import helpers


@pytest.mark.parametrize(
    "n,expected",
    [
        (1, True),
        (2, False),
        (3, True),
        (4, False),
        (5, True),
        (6, False),
        (7, True),
        (8, False),
        (9, True),
        (10, False),
        (11, True),
        (12, False),
    ],
)
def test_is_odd(n, expected):
    """Test helpers.is_odd function."""
    assert helpers.is_odd(n) is expected


@pytest.mark.parametrize(
    "n,expected",
    [
        (1, False),
        (2, True),
        (3, False),
        (4, True),
        (5, False),
        (6, True),
        (7, False),
        (8, True),
        (9, False),
        (10, True),
        (11, False),
        (12, True),
    ],
)
def test_is_even(n, expected):
    """Test helpers.is_even function."""
    assert helpers.is_even(n) is expected

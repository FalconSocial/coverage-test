"""Helper functions."""


def is_even(n: int):
    """Test if a number is even."""
    return n % 2 == 0


def is_odd(n: int):
    """Test if a number is odd."""
    return not is_even(n)

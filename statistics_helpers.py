"""Small statistics helpers used by the calculator module."""


def mean(values):
    """Return the arithmetic mean of a non-empty sequence of numbers."""
    if not values:
        raise ValueError("mean() requires at least one value")
    return sum(values) / len(values)


def median(values):
    """Return the median of a non-empty sequence of numbers."""
    if not values:
        raise ValueError("median() requires at least one value")
    ordered = sorted(values)
    midpoint = len(ordered) // 2
    if len(ordered) % 2 == 1:
        return ordered[midpoint]
    return (ordered[midpoint - 1] + ordered[midpoint]) / 2


def clamp(value, lower, upper):
    """Constrain value to the inclusive range [lower, upper]."""
    if lower > upper:
        raise ValueError("lower bound must not exceed upper bound")
    return max(lower, min(value, upper))

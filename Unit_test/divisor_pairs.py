from precompute import compute_divisor_counts, compute_matching_counts
from constants import MAX_K

_divisor_counts = compute_divisor_counts()
_matching_counts = compute_matching_counts(_divisor_counts)


def count_same_divisor_pairs(limit_value: int) -> int:
    if limit_value < 3:
        raise ValueError("Limit must be at least 3.")
    return _matching_counts[limit_value - 1]

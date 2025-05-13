from constants import MAX_K


def compute_divisor_counts() -> list[int]:
    divisor_counts = [0] * MAX_K
    for divisor in range(1, MAX_K):
        for multiple in range(divisor, MAX_K, divisor):
            divisor_counts[multiple] += 1
    return divisor_counts


def compute_matching_counts(divisor_counts: list[int]) -> list[int]:
    for number in range(2, MAX_K - 1):
        has_same_divisors = divisor_counts[number] == divisor_counts[number + 1]
        matching_counts[number] = matching_counts[number - 1] + int(has_same_divisors)

    for number in range(MAX_K - 1, MAX_K):
        matching_counts[number] = matching_counts[number - 1]

    return matching_counts

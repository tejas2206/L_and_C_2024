# Find the floor of the expected value(mean) of the subarray from Left to Right.
def process_queries():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    N, Q = map(int, data[0].split())

    arr = list(map(int, data[1].split()))

    prefix_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

    results = []
    for i in range(2, 2 + Q):
        L, R = map(int, data[i].split())
        total_sum = prefix_sum[R] - prefix_sum[L - 1]
        mean_floor = total_sum // (R - L + 1)
        results.append(str(mean_floor))

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    process_queries()
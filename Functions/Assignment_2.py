# Find the floor of the expected value(mean) of the subarray from Left to Right.
def process_queries():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    num_elements, num_queries = map(int, data[0].split())

    elements = list(map(int, data[1].split()))

    prefix_sums = [0] * (num_elements + 1)
    for index in range(1, num_elements + 1):
        prefix_sums[index] = prefix_sums[index - 1] + elements[index - 1]

    query_results = []
    for query_index in range(2, 2 + num_queries):
        left, right = map(int, data[query_index].split())
        total_sum = prefix_sums[right] - prefix_sums[left - 1]
        mean_floor = total_sum // (right - left + 1)
        query_results.append(str(mean_floor))

    sys.stdout.write("\n".join(query_results) + "\n")

if __name__ == "__main__":
    process_queries()
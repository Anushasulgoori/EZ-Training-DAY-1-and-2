def find_missing_and_repeated(arr):
    n = len(arr)
    seen = set()
    repeated = None
    total_sum = n * (n + 1) // 2
    actual_sum = 0

    for num in arr:
        if num in seen:
            repeated = num
        else:
            seen.add(num)
            actual_sum += num

    missing = total_sum - actual_sum

    return (repeated, missing)

# Example usage:
arr = [2, 1, 4, 6, 6, 5, 8, 10, 9, 7]
repeated, missing = find_missing_and_repeated(arr)
print(f"Repeated number: {repeated}")
print(f"Missing number: {missing}")

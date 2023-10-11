def find_pairs_with_sum(arr, target_sum):
    pairs = []
    seen = set()

    for num in arr:
        complement = target_sum - num

        if complement in seen:
            pairs.append((num, complement))
        
        seen.add(num)

    return pairs

# Input array and target sum
arr = [-3, 8, 7, 2, -5, 13, 18, 9, 6]
target = 20

# Find and print pairs with the target sum
pairs = find_pairs_with_sum(arr, target)
for pair in pairs:
    print(f"Pair with sum {target}: {pair}")

def find_subsets_with_sum(nums, target_sum, current_sum, index, current_subset, result):
    if current_sum == target_sum:
        result.append(current_subset[:])
        return
    
    if current_sum > target_sum or index == len(nums):
        return
    
    # Include the current element in the subset
    current_subset.append(nums[index])
    find_subsets_with_sum(nums, target_sum, current_sum + nums[index], index + 1, current_subset, result)
    
    # Exclude the current element from the subset
    current_subset.pop()
    find_subsets_with_sum(nums, target_sum, current_sum, index + 1, current_subset, result)

def subsets_with_sum(nums, target_sum):
    result = []
    find_subsets_with_sum(nums, target_sum, 0, 0, [], result)
    return result

# Example usage:
list_nums = [6, 8, 9, 5, 4, 3, 26, 2]
target_sum = 28
subsets = subsets_with_sum(list_nums, target_sum)

for subset in subsets:
    print(subset)

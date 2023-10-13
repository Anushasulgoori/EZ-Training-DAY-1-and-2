def three_pointer(nums, target):
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == target:
                return sorted([nums[i], nums[left], nums[right]])
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return None

# Sample Input
nums = [1, 2, 3, 4, 5]
target = 12

# Find the triplet and print the sorted output
result = three_pointer(nums, target)
if result:
    print(*result)
else:
    print(None)
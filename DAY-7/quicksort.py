def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Choose a pivot element
    left = [x for x in arr if x < pivot]  # Elements less than the pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot

    return quicksort(left) + middle + quicksort(right)

# Example usage
my_list = [3, 6, 8, 10, 24, 2, 1]
sorted_list = quicksort(my_list)
print(sorted_list)

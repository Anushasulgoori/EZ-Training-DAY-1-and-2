def insertion_sort(arr):
    # Start with the second element (index 1) and iterate through the list
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted into the sorted part

        # Move elements of arr[0:i] that are greater than key one position ahead
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Place the key in its correct position within the sorted part of the array
        arr[j + 1] = key

# Example usage:
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Sorted array:", arr)

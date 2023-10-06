def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage
if __name__ == "__main__":
    # Test the selection_sort function
    unsorted_list = [14,8,2,19,69,1]
    print("Unsorted list:", unsorted_list)

    selection_sort(unsorted_list)

    print("Sorted list:", unsorted_list)

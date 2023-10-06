def merge_sort(arr):
    global c
    if len(arr)<=1:
        return arr
    else:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i += 1
                k += 1
            else:
                arr[k]=right[j]
                c += len(left)-i
                j += 1
                k += 1
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
    return c
arr=[12, 11, 13, 5, 6, 7]
c=0
res=merge_sort(arr)
print(res)
def binary_search_ceil(arr,target):
    left,right=0,len(arr)
    #ceil=float('int')# +ve infinity value,it will behave as if it is infinity
    while left <=right:
        mid=left+(right-left) //2
        if arr[mid]==target:
            return arr[mid]
        elif arr[mid]<target:
            left=mid+1
        else:
            ceil=arr[mid]
            right=mid-1
    return ceil
print(binary_search_ceil([1,2,8,10,12,19],7))
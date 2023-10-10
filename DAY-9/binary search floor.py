def binary_search_floor(arr,target):
    left,right=0,len(arr)-1
    floor=-1
    while left <=right:
        mid=left+(right-left) //2
        if arr[mid]==target:
            return arr[mid]
        elif arr[mid]<target:
            floor=arr[mid]
            left=mid+1
        else:
            right=mid-1
    return floor
print(binary_search_floor([1,2,8,10,12,19],7))
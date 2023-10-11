def is_pair_exists(arr,target):
    arr.sort()
    i=0
    j=len(arr)-1
    while i<j:
        if arr[i]+arr[j]==target:return "True"
        if arr[i]+arr[j]<target:i+=1
        if arr[i]+arr[j]>target:j-=1
    return 'False'
arr=list(map(int,input().split(",")))
target=int(input())
print(is_pair_exists(arr,target))
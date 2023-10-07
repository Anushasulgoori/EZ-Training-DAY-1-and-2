def binary_search(lst,l,h,x):
    if h>=1:
        mid=(l+h)//2
        if x==lst[mid]:
            return mid
        elif x>lst[mid]:
            return binary_search(lst,mid+1,h,x)
        elif x<lst[mid]:
            return binary_search(lst,mid-1,h,x)
    else:
        return -1
lst=list(map(int,input().split()))
x=int(input())
r=binary_search(lst,0,len(lst)-1,x)
if r==-1:
    print("not found")
else:
    print("found at",r,"index")
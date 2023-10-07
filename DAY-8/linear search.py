def linear_search(lst,x):
    flag=0
    for i in range(len(lst)):
        if x==lst[i]:
            flag=1
            return i
    if flag==0:
        return -1
list=list(map(int,input().split()))
x=int(input())
r=linear_search(list,x)
if r==-1:
    print("element is not found")
else:
    print("element is found at",r,"index")
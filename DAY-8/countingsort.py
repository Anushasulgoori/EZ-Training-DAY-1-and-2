def count_sort(lst):
    s=len(lst)
    count_arr=[0]*s
    result_arr=[0]*s
    for i in range(s):
        count_arr[lst[i]]+=1
    for i in range(1,s):
        count_arr[i]+=count_arr[i-1]
    n=s-1
    while n>=0:
        result_arr[count_arr[lst[n]]-1]=lst[n]
        count_arr[lst[n]]-=1
        n-=1
    for i in range(0,s):
        lst[i]=result_arr[i]
lst=list(map(int,input().split()))
count_sort(lst)
for i in range(0,len(lst)):
    print(lst[i],end=' ')
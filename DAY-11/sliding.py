#sliding window mechanism
def sub_arr(arr,k,n):
    i=0
    j=k-1
    s=0
    
    while j<n:
        if i==0:
            s=sum(arr[i:j+1])
            ps=s
        else:
            cs=ps-arr[i-1]+arr[j]
            s=max(s,cs)
            ps=cs
        i+=1
        j+=1
    return s
            
        
    
        
arr=list(map(int,input().split(",")))
k=int(input())
n=len(arr)
print(sub_arr(arr,k,n))
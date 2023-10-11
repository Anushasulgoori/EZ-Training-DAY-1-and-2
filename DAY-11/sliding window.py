def sub_array(arr,k):
    sum_array=0
    i,j=0,k-1
    while j<len(arr):
        if i==0:
            sum_array=sum(arr[i:j+1])
            ps=sum_array
        else:
            cs=ps-arr[i-1]+arr[j]
            sum_array=max(sum_array,cs)
            ps=cs
        i+=1
        j+=1
    return  sum_array
print(sub_array([-3,20,3,-9,18,-45,23,67],3))
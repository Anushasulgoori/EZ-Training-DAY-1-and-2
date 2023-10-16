def hollow_pyramid(n):
    row = n
    col = 2*n-1
    start , end = n-1 , n-1
    var = 2
    var2 = 1
    for i in range(row):
        for j in range(col):
            if (j==start or j==end) and i!=n-1:
                if start == end:
                    print(1,end=" ")
                elif j==start:
                    print(1,end=" ")
                else:
                    print(var,end=" ")
                    var+=1
            elif i==n-1 and (j>=start and j<=n-1):
                print(var2,end=" ")
                var2+=1
            else:
                print(" ",end="")
            
        print()
        start-=1
        end+=1



hollow_pyramid(7)
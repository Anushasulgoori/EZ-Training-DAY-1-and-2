def pyramid(n):
    row = n
    col = 2*n-1
    start , end = n-1 , n-1
    for i in range(row):
        for j in range(col):
            if j>=start and j<=end:
                print(" ",end="")
            else:
                print("*",end="")
        print()
        start-=1
        end+=1
pyramid(5)
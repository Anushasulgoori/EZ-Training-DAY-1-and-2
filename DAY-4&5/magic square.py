# Initialize a 3x3 magic square with zeros
magic_square = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
n = 3
i,j=0,n//2
for num in range(1, n**2 + 1):
    magic_square[i][j] = num
    new_i,new_j = (i - 1) % n,(j + 1) % n
    if magic_square[new_i][new_j] != 0:
        i = (i + 1) % n
    else:
        i, j = new_i, new_j
for row in magic_square:
    for num in row:
        print(f"{num:2d}", end=" ")
    print()
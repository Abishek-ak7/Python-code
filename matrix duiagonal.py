R, C = map(int, input().split())

# read the matrix
matrix = [list(map(int, input().split())) for i in range(R)]

# print the matrix diagonally
for i in range(R+C-1):
    for j in range(max(0, i-C+1), min(i+1, R)):
        print(matrix[j][i-j], end=' ')
    print()

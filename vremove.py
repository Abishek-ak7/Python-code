def print_matrix_diagonally(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows - 1, -1, -1):
        row, col = i, 0
        while row < rows and col < cols:
            print(matrix[row][col], end=" ")
            row += 1
            col += 1
        print()

    for i in range(1, cols):
        row, col = 0, i
        while row < rows and col < cols:
            print(matrix[row][col], end=" ")
            row += 1
            col += 1
        print()

# Ask for user input
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix = []

# Read the matrix elements from user input
for i in range(rows):
    row = list(map(int, input("Enter the elements of row %d (separated by space): " % (i+1)).split()))
    matrix.append(row)





print_matrix_diagonally(matrix)

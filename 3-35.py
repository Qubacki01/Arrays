###
#
#

def transpose_matrix(m):    # Create matrix - each row is a column of the og matrix
    transposed = []
    for j in range(len(m[0])):  # Go over columns of original matrix. (len(m[0])) -> nr of columns
        row = [m[i][j] for i in range(len(m))]  # For each column create new row
        transposed.append(row)  # Add row to transposed matrix
    return transposed


def print_matrix(matrix):       # Print the matrix
    for row in matrix:
        print(' '.join(map(str, row)))


matrix_1 = [        # OG Matrix
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_2 = [        # OG Matrix
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0],
    [5, 6, 7, 8, 0]
]


print("Transpose of Matrix 1:")
transposed_1 = transpose_matrix(matrix_1)
print_matrix(transposed_1)
print()

print("Transpose of Matrix 2:")
transposed_2 = transpose_matrix(matrix_2)
print_matrix(transposed_2)

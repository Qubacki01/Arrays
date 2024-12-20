###
#
#

def identity_matrix(n):      # Create an identity matrix of size n
    matrix = []              # Create list for rows
    for i in range(n):       # Row index
        row = [1 if j == i else 0 for j in range(n)]     # Create row -diagonal-(1 on diagonal else 0)
        matrix.append(row)
    return matrix


def print_matrix(matrix):           # Print a 2D matrix in rows and columns
    for row in matrix:
        print(' '.join(map(str, row)))




print("Identity Matrix of size 3:")
matrix_3 = identity_matrix(3)
print_matrix(matrix_3)
print()

print("Identity Matrix of size 5:")
matrix_5 = identity_matrix(5)
print_matrix(matrix_5)
print()

print("Identity Matrix of size 8:")
matrix_8 = identity_matrix(8)
print_matrix(matrix_8)

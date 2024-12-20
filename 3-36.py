###
#
#


def flatten_2d_to_1d(matrix):       # Convert 2D array to 1D array using nested loops
    flattened = []
    for row in matrix:          # Go over each row in the matrix
        for element in row:     # Go over each element in the row
            flattened.append(element)  # Append the element to the flattened list
    return flattened


def print_array(array):     # Print the 1D array
    print("1D Array:", array)

matrix_1 = [
    [2, 3],
    [1, 5]
]

matrix_2 = [
    [5, 0, 3, 7, 5],
    [9, 0, 9, 1, 2]
]

matrix_3 = [
    [2, 1],
    [3, 5],
    [7, 4],
    [2, 6]
]


flattened_matrix_1 = flatten_2d_to_1d(matrix_1)     # Flattening the 2D arrays
flattened_matrix_2 = flatten_2d_to_1d(matrix_2)
flattened_matrix_3 = flatten_2d_to_1d(matrix_3)


print("Flattened Matrix 1:")
print_array(flattened_matrix_1)

print("Flattened Matrix 2:")
print_array(flattened_matrix_2)

print("Flattened Matrix 3:")
print_array(flattened_matrix_3)

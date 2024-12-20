###
#
#

array = [[-38, 19], [5, 40], [-7, 11], [29, 16]]


min_value = float('inf')    # Setting initial minimum to +inf
max_value = float('-inf')   # Setting initial maximum to -inf
min_position = (-1, -1)     # Row and column of min value
max_position = (-1, -1)     # Row and column of max value

                                    # Looping through each row and column
for i in range(len(array)):         # Iterate over rows
    for j in range(len(array[i])):  # Iterate over columns
        value = array[i][j]         # Compare arr to value
        
        if value < min_value:       # Check for the minimum value
            min_value = value
            min_position = (i, j)   # Update position for min value
        
        if value > max_value:       # Check for the maximum value
            max_value = value
            max_position = (i, j)   # Update position for max value


print(f"Smallest value: {min_value} at position: Row {min_position[0]}, Column {min_position[1]}")
print(f"Largest value: {max_value} at position: Row {max_position[0]}, Column {max_position[1]}")

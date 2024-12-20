###
#
#

def create_2d_arr(x, y):        # Create a 2D array (x by y) filled with 0

    array = []      # Empty arr
    
    for i in range(x):      # Loop to create rows
        row = [0] * y       # Create a row with 'y' 0
        array.append(row)   # Add the row to the array
    
    return array

array = create_2d_arr(3, 5)

for row in array:
    print(row)

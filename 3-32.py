###
#
#

array = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

def print_array(arr):       # Print the array in rows and columns
    for row in arr:
        print(' '.join(map(str, row)))


print("Array before swapping rows: ") # Print array before swapping rows
print_array(array)


array[0], array[-1] = array[-1], array[0]   # Swap first and last rows 

print()
print("Array after swapping rows:")
print_array(array)

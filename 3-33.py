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


print("Array before swapping columns:")     # Print array before swapping columns
print_array(array)


for row in array:                           # Swapping the first and last columns
    row[0], row[-1] = row[-1], row[0]

print()
print("Array after swapping columns:")
print_array(array)

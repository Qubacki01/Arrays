###
#
#

def bubble_sort(arr):
    n = len(arr)            # Get array length
    for i in range(n):      # Outer loop controls nr passes
        for j in range(n - i - 1):      # Inner loop to compare adjacent; its length decreases
            if arr[j] > arr[j + 1]:     # Is current elem > next elem
                arr[j], arr[j + 1] = arr[j + 1], arr[j]     # Swap if neccecery
    return arr


array1 = [78, 12, 35, 64, 91, 42, 57]
array2 = [9, 3, 5, 8, 1, 7]
array3 = [14, 19, 8, 3, 17, 10, 11]

print("Original array1:", array1)
print("Sorted array1:", bubble_sort(array1))

print()

print("Original array2:", array2)
print("Sorted array2:", bubble_sort(array2))

print()

print("Original array3:", array3)
print("Sorted array3:", bubble_sort(array3))

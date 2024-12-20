###
#
#

def print_unique_elements(array):
    unique_elements = []
    
    for num in array:
        if array.count(num) == 1 and num not in unique_elements:    # Count instances of elem in array
            unique_elements.append(num)                             # and place new unique elem in list
    
    print("Unique elements:", *unique_elements)

array = [2, 3, 2, 5, 8, 1, 9, 8]

print("Array:", *array)
print_unique_elements(array)

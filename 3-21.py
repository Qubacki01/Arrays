###
#
#

def is_subset(arr1, arr2):
    return all(elem in arr2 for elem in arr1)   # Check if all elements of arr1 are in arr2

arr1 = [1, 3, 5]
arr2 = [5, 3, 1, 7, 9, 2]

result = is_subset(arr1, arr2)

if result:
    print(f"Array {arr1} is a subset of {arr2}")
else:
    print(f"Array {arr1} is not a subset of {arr2}")

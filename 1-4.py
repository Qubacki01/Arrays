###
# Prints some array elements
#

arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Last value', arr[4])
print('Last but one value', arr[3])
print('Sum of the first and last', arr[0] + arr[4])
print('Middle value', arr[len(arr) // 2])
print('All array values separated by space:', end = " ")
for value in arr:
    print(value, end = " ")
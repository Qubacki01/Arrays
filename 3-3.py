###
#
#

arr = [8, 2, 5, 1, 9]

print("Array:", *arr)       # Get space between elem

power_arr = [x ** 2 for x in arr]
print("2nd power:", *power_arr)

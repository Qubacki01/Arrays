###
#
#

arr = [-15, 8, -31, 47, -2, 19]

max_value = arr[0]
min_value = arr[0]

for num in arr:
    if num > max_value:
        max_value = num  # Update max with num if number is larger
    if num < min_value:
        min_value = num  # Update min if number is smaller


print("Maximum number:", max_value)
print("Minimum number:", min_value)

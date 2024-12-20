###
#
#

arr = [34, 7, 19, 4, 21, 8]

even_count = 0
i = 0

while i < len(arr):
    if arr[i] % 2 == 0:     # Even check
        even_count += 1     # Increase count
    i += 1                  


print("Even values count:", even_count)

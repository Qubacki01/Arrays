###
#
#

arr = [15, 8, 31, 47, 2, 19]


total_sum = 0
index = 0

while index < len(arr):     
    total_sum += arr[index] # Adds value of element at current index
    index += 1

mean = total_sum / len(arr)

print("Arithmetic mean:", mean)
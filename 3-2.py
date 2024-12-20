###
#
#

arr = [15, 8, 31, 47, 2, 19]

print("existed array:", *arr)       # Get space between elem

print("reverse array:", end=" ")
for num in reversed(arr):
    print(num, end=" ")

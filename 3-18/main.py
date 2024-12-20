###
#
#

import MyArrays

numbers = [7, 3, 8, 5, 2]

print("Numbers:", MyArrays.array_to_string(numbers))
print("Second largest number:", MyArrays.second_largest(numbers))
print("Median:", MyArrays.median(numbers))
print("Smallest and largest number:", ", ".join(map(str, MyArrays.smallest_largest(numbers))))
print("Numbers as a string:", MyArrays.array_to_string(numbers))

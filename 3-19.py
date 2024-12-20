###
#
#

def count_greater_elements(arr, value): # How many elem in array are greater than given value
    count = 0               # Stores num of elem > given value
    for number in arr:
        if number > value:
            count += 1
    return count

arr = [3.14, 7.56, 5.89, 8.32, 2.17, 6.45, 4.72, 9.11, 3.98, 6.78]
value = float(input("Enter a value to compare: "))

result = count_greater_elements(arr, value)     # Count of elem bigger than given value


print(f"The number of elements greater than {value} is: {result}")

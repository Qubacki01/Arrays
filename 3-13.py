###
#
#

def occurs(number, array):  # Check if in array
    return number in array

def main():
    array = [15, 38, 7, 23, 14]
    
    number = int(input("Enter a number: "))
    
    print("Array:", *array) # (separate with space)
    if occurs(number, array):   # Check if present in array and print 
        print(f"Result: Number {number} appears in the array")
    else:
        print(f"Result: Number {number} does not appear in the array")

main()

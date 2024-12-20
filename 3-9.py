###
#
#

def compare(array1, array2):
    return array1 == array2     # True if same, False if not


array1_1 = ["water", "book", "sky"]
array2_1 = ["water", "book", "sky"]

array1_2 = [True, False]
array2_2 = [True, False, True]

array1_3 = [5, 3, 1]
array2_3 = [5, 3, 1]

array1_4 = [3, 2, 1]
array2_4 = [3, 2]


def print_comparison(array1, array2):
    print("Array1:", " ".join(map(str, array1)))    # Change to string; add space
    print("Array2:", " ".join(map(str, array2)))
    if compare(array1, array2):
        print("Comparison: Arrays are the same\n")      # \n - move to next line
    else:
        print("Comparison: Arrays are not the same\n")


print_comparison(array1_1, array2_1)
print_comparison(array1_2, array2_2)
print_comparison(array1_3, array2_3)
print_comparison(array1_4, array2_4)

###
#
#

def separate_even_odd(arr):     # Separate even and odd numbers
    even_numbers = []
    odd_numbers = []

    for num in arr:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    return even_numbers + odd_numbers     # Join even and odd list (even then)

arr = [7, 9, 2, 4, 5, 6]

arr = separate_even_odd(arr)

print("arr =", arr)

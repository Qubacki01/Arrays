###
#
#

import random

def rand_elem(array):       # Return randomly selected elem from array
    return random.choice(array)

arr = [14, 3, 97, 23, 15, 0, 31]

print("Randomly selected elements:")
for _ in range(5):          # Print 5 random elem
    print(rand_elem(arr))

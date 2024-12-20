###
#
#

import random

arr1 = [3, 7, 1, 0, 4]
print("arr1:", arr1)

arr2 = [[2, 3], [7, 1], [0, 4]]
print("arr2:", arr2)

arr3 = [7 for i in range(5)]
print("arr3:", arr3)

arr4 = [i for i in range(1, 10)]
print("arr4:", arr4)

arr5 = [i * 2 for i in range(1, 10)]    
print("arr5:", arr5)

arr6 = [random.randint(1, 20) for i in range(10)]   # 10 rand int between 1 and 20
print("arr6:", arr6)

arr7 = [[] for i in range(5)]   # Array with 5 empty sub-arrays
print("arr7:", arr7)

arr8 = [[1 for i in range(2)] for j in range(4)]  # All elements 1
print("arr8:", arr8)

arr9 = [[random.randint(1, 20) for i in range(3)] for j in range(5)]    # Array w/ 5 rows and 3 columns with random integers (1 - 20)
print("arr9:", arr9)

arr10 = [4, 0, 3]
print("arr10:", arr10)

arr11 = [0] * 15
print("arr11:", arr11)

arr12 = [random.randint(1, 30) for i in range(10)]
print("arr12:", arr12)

arr13 = [random.choice([0, 1]) for i in range(20)]  # 20-element array filled with 0 or 1 randomly
print("arr13:", arr13)

arr14 = [[False for i in range(2)] for j in range(5)]   ## 2D array with 5 rows and 2 columns filled with False
print("arr14:", arr14)

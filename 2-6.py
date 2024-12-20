###
# Matrix
#

matrix = [
   [0, 0, 0],
   [0, 0, 0],
   [0, 0, 0]
]

for i in range(len(matrix)):    # Get number of rows
   matrix[i][i] = 1             # Replace values of main diagonal with 1


for row in matrix:
   print(" ".join(map(str, row)))   # Convert to string and give space

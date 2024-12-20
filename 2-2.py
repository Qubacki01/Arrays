###
# Tic-Tac-Toe
#

# 3x3 Tic-Tac-Toe board
tic_tac_toe_board = [
   ['X', 'O', 'X'],
   [' ', 'X', 'O'],
   ['O', ' ', 'X']
]

for row in tic_tac_toe_board:       # Loop each row
    for element in row:             # Loop each elem in row
        print(element, end=" ")     # Print elem and space
    print()

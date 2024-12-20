###
#
#

def create_multiplication_table(x, y):  # Create a multiplication table
    table = []
    
    for i in range(1, x + 1):       # Loop rows (inclusive) 
        row = []
        for j in range(1, y + 1):   # Loop columns (incl)
            row.append(i * j)       # Calc prod of row index by column index
        table.append(row)
    
    return table

array = create_multiplication_table(5, 5)

for row in array:
    print(' '.join(map(str, row)))

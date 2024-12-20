###
#  A program that calculates which expense category was the most expensive
#

categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

# Find the index of the maximum expense
max_expense_index = expenses.index(max(expenses))       # Highest value from list and its index


print("The most expensive category is:", categories[max_expense_index]) # Apply index number
print("Expense:", expenses[max_expense_index])

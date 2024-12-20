###
#   Total expenses
#

# Weekly expenses for different categories
# [Food, Transport, Utilities]

monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]


total_food = 0
total_transport = 0
total_utilities = 0

week_totals = []

for week in monthly_expenses:   # Loop each week's expenses
    total_food += week[0]       # 0,1,2 - indices for each cate
    total_transport += week[1]
    total_utilities += week[2]
    week_totals.append(sum(week))   # Total for each week and add to list

total_month = sum(week_totals)

# Print the expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', total_food)
print('Transport:', total_transport)
print('Utilities:', total_utilities)
print('Week 1:', monthly_expenses[0])
print('Week 2:', monthly_expenses[1])
print('Week 3:', monthly_expenses[2])
print('Week 4:', monthly_expenses[3])
print('---------------')
print('TOTAL:', total_month)
print()

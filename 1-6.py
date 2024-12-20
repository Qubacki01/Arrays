###
# Returns the name of the day of the week for a day number 
#

def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[n - 1]  # Because we want monday to be on index 1

print(weekday(1))
print(weekday(4))
print(weekday(7))

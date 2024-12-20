###
#
#

names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

print("Names:", " ".join(names))    # Print list with spaces


longest_name = names[0]  # Start with first name
big_length = len(longest_name) # Set character length to first name


for name in names:          # Find the longest name
    if len(name) > big_length:
        longest_name = name
        big_length = len(name)

# Print the longest name
print("Longest name:", longest_name)

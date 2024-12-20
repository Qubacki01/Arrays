###
# List of popular computer games
#

computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

computer_games.sort()       # Sort alphabetically

index = 1       # Numbering

while index <= len(computer_games):     # Loop runs until index = list length
    print(f"{index}. {computer_games[index - 1]}")
    index += 1

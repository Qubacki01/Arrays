###
#
#

# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):         # Total seats
   return len(seats) * len(seats[0])        # rows * seats in row 1

def seats_available(seats):     # Available seats
   return sum(row.count('A') for row in seats)

def seats_booked(seats):        # Booked seats
   return sum(row.count('B') for row in seats)

def seat_status(seats, row, place):     # Status of a given seat
   if seats[row-1][place-1] == 'A':     # Get index (from base-1 to base-0)
      return "Available"
   else:
      return "Booked"


print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:', seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))

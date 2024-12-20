###
#
#

# Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
meal_plan = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
   ["Pancakes", "Sandwich", "Steak"],
   ["Smoothie", "Chicken Wrap", "Salmon"],
   ["Eggs", "Pasta", "Soup"],
   ["Toast", "Burrito", "Pizza"],
   ["Cereal", "Salad", "Fish Tacos"],
   ["Bagel", "Rice and Beans", "Stir-fry"]
]

def weekday(n):
   weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday"]
   return weekdays[n-1]     # Get index (0-6)


def day_meal_plan(meal_plan, day_number):   # Day number later "i"
   day_meals = meal_plan[day_number - 1]    # Get meals for given day and [get index - from base 1 to 00]
   return ', '.join(day_meals)      # Join items in "meals" into string


def print_weekly_meal_plan(meal_plan):
   print("WEEKLY MEAL PLAN")
   print("(Breakfast, Lunch, Dinner)")
   print("==========================")

   for i in range(1, 8):           # Loop through the days of the week
      day_name = weekday(i)        # Get the name of the day
      meals_for_day = day_meal_plan(meal_plan, i)       # Get the meal plan for the day
      print(f"{day_name}: {meals_for_day}")


print_weekly_meal_plan(meal_plan)
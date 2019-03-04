# number = int(input('Enter a natural number'))
# if number > 0:
#     for number in range(0, number + 1):
#         print(number)
#         if number > number:
#             break
# else:
#      print('You did not select a natural number!')

# Do your work for this exercise in a file named 4.3_control_structures_exercises.py.

# 1. Conditional Basics

# a. prompt the user for a day of the week, print out whether the day is Monday or not
# day_of_week = input('Name a day of the week:  ')
# if day_of_week == 'Monday':
#     print('Monday')
# else: 
#     print('This is not Monday!')

# b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

# day_of_week = input('Name a day of the week.')
# if day_of_week == 'Monday' or day_of_week == "Tuesday" or day_of_week == 'Wednesday'or day_of_week =='Thursday' or day_of_week == 'Friday':
#     print('You have chosen a week day.')
# else: 
#     print('You have chosen a weekend!')

# c. create variables and make up values for
#    the number of hours worked in one week
#    the hourly rate
#    how much the week's paycheck will be
#    write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

# hours_worked_per_week = int(input('How many hours do you work per week?'))
# hourly_rate = int(input('What is your hourly rate?'))
# if hours_worked_per_week <= 40:
#     weekly_rate = hours_worked_per_week * hourly_rate
#     print('You get paid', weekly_rate, " dollars per week.")
# else:
#     if hourly_rate > 40:
#         time_and_a_half = weekly_rate + (hours_worked_per_week  * (hourly_rate * 1.5)
#         print('You got paid', time_and_a_half, 'dollars!')

# 2. Loop Basics

# a. While

#   Create an integer variable i with a value of 5.
#   Create a while loop that runs so long as i is less than or equal to 15
#   Each loop iteration, output the current value of i, then increment i by one.

# i = 5
# while i <= 15:
#     print(i)
#     i += 1

# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
# Alter your loop to count backwards by 5's from 100 to -10.
# Create a while loop that starts at 2, and displays the number squared on each 
# line while the number is less than 1,000,000. Output should equal:



# 1. Conditional Basics

# a. prompt the user for a day of the week, print out whether the day is Monday or not

day_of_week = input('Name a day of the week:  ')
if day_of_week == 'Monday':
    print('Monday')
else: 
    print('This is not Monday!')

# b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

day_of_week = input('Name a day of the week.')
if day_of_week == 'Monday' or day_of_week == "Tuesday" or day_of_week == 'Wednesday'or day_of_week =='Thursday' or day_of_week == 'Friday':
    print('You have chosen a week day.')
else: 
    print('You have chosen a weekend!')

# c. create variables and make up values for
#    the number of hours worked in one week
#    the hourly rate
#    how much the week's paycheck will be
#    write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

hours_worked_per_week = int(input('How many hours do you work per week?'))
hourly_rate = int(input('What is your hourly rate?'))
if hours_worked_per_week <= 40:
    weekly_rate = hours_worked_per_week * hourly_rate
    print('You get paid', weekly_rate, " dollars per week.")
else:
    if hourly_rate > 40:
        time_and_a_half = weekly_rate + (hours_worked_per_week  * (hourly_rate * 1.5)
        print('You got paid', time_and_a_half, 'dollars!')

# 2. Loop Basics

# a. While

#   i. Create an integer variable i with a value of 5.
#   Create a while loop that runs so long as i is less than or equal to 15
#   Each loop iteration, output the current value of i, then increment i by one.

i = 5
while i <= 15:
    print(i)
    i += 1

# ii. Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

i = 0
while i <= 100:
    print(i)
    i += 2

# iii. Alter your loop to count backwards by 5's from 100 to -10.

i = 100
while i >= -10:
    print(i)
    i -= 5

# iiii. Create a while loop that starts at 2, and displays the number squared on each 
# line while the number is less than 1,000,000. 

i = 2
while i < 1_000_000:
    print(i)
    i = i ** 2

#  iiiii. Write a loop that uses print to create the output shown below.


# 100
# 95
# 90
# 85
# 80
# 75
# 70
# 65
# 60
# 55
# 50
# 45
# 40
# 35
# 30
# 25
# 20
# 15
# 10
# 5   

i = 100
while i >= 5:
    print(i)
    i -= 5
# alternate method

for n in range(100, 0, -5):
    print(n)

# b. For Loops

# i. Write some code that prompts the user for a number, 
# then shows a multiplication table up through 10 for that number.

user_input = int(input('Please enter a number: '))
for n in range(0,10):
    mult_table = user_input * n
    n += 1
    print(n, "*", user_input, '=', mult_table)    

# alternate method
x = int(input('Please enter a number:  '))
for n in range(1, 11):
    output = '{} X {} = {}' .format(x, n, x * n)
    print(output)

#  ii. Create a for loop that uses print to create the output shown below.
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

for n in range(1, 10):
    print(str(n) * n)

# c break and continue

# i. Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.

user_input = input('Please enter an odd number between one and fifty:  ')
while not user_input.isdigit() or int(user_input) > 50 or int(user_input) % 2 == 0:
    user_input = input('Hey! You did not give me an odd number, try again!')
user_input = int(user_input)
print('Number to skip is:  ', user_input)
for i in range(1, 51):
    if i % 2 == 0:
        continue
    if i == user_input:
        print('Yikes! Skipping number: the_number_entered')
    else: 
         print('Here is odd number: ', i)

# d The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)

user_input = input('Enter a positive number: ')
while not user_input.isdigit() or not int(user_input) >= 0:
    user_input = input('You did not enter a positive number, try again!')
user_input = int(user_input)
for pos_int in range(0, user_input + 1):
    print(pos_int)

# e Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.

user_input = input('Enter a positive number: ')
while not user_input.isdigit() or not int(user_input) >= 0:
    user_input = input('You did not enter a positive number, try again!')
user_input = int(user_input)
for pos_int in (range(user_input, 0)):
    print(pos_int)

# 3. Fizzbuzz
# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

for n in range(1, 16):
    if n % 15 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)

# alternate solution
for n in range(1, 111):
    output = ''
    if n % 3 == 0:
        output += 'Fizz'
    if n % 5 == 0:
        output = f'{output}Buzz'
    if n % 7 == 0:
        output = '%sBang' % output

# 4 Display a table of powers.
# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.

user_input = input('What would you like your number to go to?')
while not user_input.isdigit() or not int(user_input) >= 0 or user_input == 'no':
user_input = input('You did not enter a positive number, try again!')
user_input = int(user_input)
print('Here is your table!')
print('number', 'squared', 'cubed')
for n in range(0, user_input + 1):
    squared = n * n
    cubed = n * n * n
    print( n, squared, cubed)
    continue
    if user_input == "yes":
        user_input = input('Would you like to continue?')
    else:
        break

#  Bonus:
upper_bound = int(input('Enter a number: '))
n = 1

print('number | squared | cubed')
print('------ | ------- | -----')
for n in range(1, upper_bound + 1):
    right-aligned (default)
    print('{:6} | {:7} | {:5}'.format(n, n ** 2, n ** 3))
    left-aligned
    print('{:<6} | {:<7} | {:<5}'.format(n, n ** 2, n ** 3))
    center-aligned
    print('{:^6} | {:^7} | {:^5}'.format(n, n ** 2, n ** 3))

#  5.Convert given number grades into letter grades.

# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:

# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0  

grade = int(input('Enter a number grade: ')) 
user_wants_to_continue = 'yes'
while user_wants_to_continue == 'yes':
    grade = int(input('Enter a number grade: '))

    if grade >= 88:
        print('A')
    elif grade >= 80:
        print('B')
    elif grade >= 67:
        print('C')
    elif grade >= 60:
        print('D')
    elif grade >= 0:
        print('F')

    user_wants_to_continue = input('Do you want to continue? ')
# 
# 1. Define a function named is_two. 
#     It should accept one input and return 
#     True if the passed input is either the number or the string 2, 
#     False otherwise.

def is_two(n):
    if n == 2 or n == '2':
        return True
    else:
        return False

def is_two(n):
    return n == 2 or n =='2'

print(is_two(5))
print(is_two(2))

# 2. Define a function named is_vowel. 
#   It should return True if the passed string is a vowel, False otherwise.

def is_vowel(v):
    if v == 'a' or v == 'e' or v == 'i' or v == 'o' or v == 'u':  
          return True
    else:
        return False

print(is_vowel('a'))
print(is_vowel('t'))

def is_vowel(v):
    if v in ['a', 'e', 'i', 'o', 'u']:
        return True
    else: 
        return False

def is_vowel(a_string):
    return a_string in 'aeiou'

print(is_vowel('a'))
print(is_vowel('b'))


# 3.Define a function named is_consonant. 
#     It should return True if the passed string is a consonant, False otherwise. 
#     Use your is_vowel function to accomplish this.

def is_consonant(c):
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':  
          return False
    else:
        return True

def is_consonant(c):
    if is_vowel(c):
        return False
    else:
        return True

def is_consonant(a_string):
    return not is_vowel(a_string)

print(is_consonant('f'))
print(is_consonant('i'))

# 4. Define a function that accepts a string that is a word. 
#     The function should capitalize the first letter of the word 
#     if the word starts with a consonant.

def cap_first(word):
    if is_consonant(word[0]):
        word = word.capitalize()
    return word
        

print(cap_first('queen'))
print(cap_first('erin'))

# 5. Define a function named calculate_tip. It should accept a tip percentage 
#     (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(percentage, bill):
    tip = percentage * bill
    return tip
    
print(calculate_tip(.2 , 20))

# 6. Define a function named apply_discount. It should accept a original price, 
#     and a discount percentage, and return the price after the discount is applied.

def apply_discount(ori_price, percentage):
    discount = ori_price * percentage
    final_price = ori_price - discount
    return final_price

print(apply_discount(50, .25))

# 7. Define a function named handle_commas. 
#     It should accept a string that is a number that contains commas in it as input, 
#     and return a number as output.

def handle_commas(string):
    newstr = string
    for x in string.lower():
        if x == ',':
            newstr = newstr.replace(x, '')
    return newstr
    #need to update

    
print(handle_commas('1,000,000'))

# 8. Define a function named get_letter_grade. It should 
#     accept a number and return the letter grade associated with that number (A-F).

def get_the_letter_grade(x):
        if x >= 90:
            return 'A'
        elif x >= 80:
            return 'B'
        elif x >= 70:
            return 'C'
        else:
            return 'F'
    
print(get_the_letter_grade(64))

# 9. Define a function named remove_vowels that accepts a string
#  and returns a string with all the vowels removed.

def remove_vowels(v):
    newstr = v.lower()
    vowels = ('a', 'e', 'i', 'o', 'u')
    for x in v:
        if x in vowels:
            newstr = newstr.replace(x, '')
    return newstr
    
print(remove_vowels('igloo'))

# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed

LETTERS ='_abcdefghijklmnopqrstuvwxyz'
def normalize_name(a_string):
    a_string = a_string.strip().replace(' ','_').lower()
    valid_characters = []
    for character in a_string:
        if character in LETTERS:
            valid_characters.append(character)

    return ''.join(valid_characters)

print(normalize_name('Name'))
print(normalize_name('First Name'))
print(normalize_name('% Completed'))


    
# 11.Write a function named cumsum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumsum([1, 1, 1]) returns [1, 2, 3]
# cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumsum(numbers):
    sums = [numbers[0]]
    for current_number in numbers[1:]:
        last_number = sums[-1]
        next_number = last_number + current_number
        sums.append(next_number)
    return sums

print(cumsum([1, 2, 3]))


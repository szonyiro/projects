import random

"""Variables with strings"""
letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "!#$%&?@*+"

"""strings converted to lists"""
list_of_letter = list(letters) + list(letters.upper())
list_of_numbers = list(numbers)
list_of_symbols = list(symbols)

# """For loop list converting"""
# for letter in letters:
#     """Creates a list from variable called 'letters'. """
#     list_of_letter.append(letter)
#     list_of_letter.append(letter.upper())
#
# for number in numbers:
#     """Creates a list from variable called 'numbers'. """
#     list_of_numbers.append(number)
#
# for symbol in symbols:
#     """Creates a list from variable called ' symbols'. """
#     list_of_symbols.append(symbol)

# print(list_of_letter)
# print(list_of_numbers)
# print(list_of_symbols)

"""Asking for user input to determine how many letters, numbers and symbols to use for the password"""
no_letters = int(input("How many letters?: "))
no_numbers = int(input("How many numbers?: "))
no_symbols = int(input("How many symbols?: "))

"""For loops to pick random letters, numbers and symbols """
password = ""
for random_letter in range(no_letters):
    password += random.choice(list_of_letter)
for random_number in range(no_numbers):
    password += random.choice(list_of_numbers)
for random_symbol in range(no_symbols):
    password += random.choice(list_of_symbols)

"""Passwords is converted into a list then the picked letters, numbers and symbols are randomly shuffled around"""
password = list(password)
random.shuffle(password)

"""Join the elements of the list into 1 string"""
print("".join(password))


from random import randbytes, randint, random
from random import choice
from operator import length_hint
from random import shuffle

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","k", "l","m","n","o","p","q",
"r","s","t","u","v","w","x","y","z","A","B","C","D","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '{', '}', '[', ']', '\\', '|',
    ':', ';', '"', "'", '<', '>', ',', '.', '?', '/',
    '~', '`']

print("Welcome to the PyPassword Generator!")
random_numbers = choice(numbers)
random_symbols = choice(symbols)

password = ""
letters_user = int(input("How many letters would you like in your password?"))
num_user = int(input("How many numbers would you like in your password?"))
symbol_user = int(input("How many symbols would you like in your password?"))

list_of_choices = []
for char in range(1, letters_user + 1):
    random_letters = choice(letters)
    password += random_letters
    list_of_choices.append(random_letters)
for num in range(1, num_user + 1):
    random_numbers = choice(numbers)
    password += random_numbers
    list_of_choices.append(random_numbers)
for symbol in range(1, symbol_user + 1):
    random_symbols = choice(symbols)
    password += random_symbols
    list_of_choices.append(random_symbols)
print("You password is: " + password)
print()
shuffle(list_of_choices)
print("Between this chars: ")
print(list_of_choices)

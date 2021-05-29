'''
Password generator
'''
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


n_letters = int(input('How many letters in the password do you want?: '))
n_numbers = int(input('How many numbers in the password do you want?: '))
n_symbols = int(input('How many symbols in the password do you want?: '))

password = ''

for _ in range(n_letters):
    password += random.choice(letters)

for _ in range(n_numbers):
    password += random.choice(numbers)

for _ in range(n_symbols):
    password += random.choice(symbols)

password = ''.join(random.sample(password, len(password)))

print(password)
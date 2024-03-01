#code by saurabh bhosale
import random

n_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C',
             'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'
             , 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

n_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

n_symbols = ['@','#']

print("Welcome to Password Generator")

letters = int(input("How many letters do you want in your password?\n"))
symbols = int(input("How many symbols do you want in your password?\n"))
numbers = int(input("How many numbers do you want in your password?\n"))

password_list = []

for _ in range(letters):
    char = random.choice(n_letters)
    password_list.append(char)

for _ in range(symbols):
    char = random.choice(n_symbols)
    password_list.append(char)

for _ in range(numbers):
    char = random.choice(n_numbers)
    password_list.append(char)

random.shuffle(password_list)

password = "".join(password_list)
print("Your generated password is:", password)

from random import choice, shuffle

# making password_generator with help of python list and random module
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
              'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
number_of_characters = int(input("How many letters would you like in your password?\n"))
number_of_symbols = int(input(f"How many symbols would you like?\n"))
number_of_numbers = int(input(f"How many numbers would you like?\n"))
password_list = []

for char in range(1, number_of_characters + 1):
    password_list.append(choice(characters))

for char in range(1, number_of_symbols + 1):
    password_list += choice(symbols)

for char in range(1, number_of_numbers + 1):
    password_list += choice(numbers)
# making our list to shuffle, so we can get mixed variables or characters
shuffle(password_list)
# for joining and printing it as a string

password = ""
for char in password_list:
    password += char

print(f"Your Password is: \n {password}")
print("\n Made By Anushka")

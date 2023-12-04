import random
import string

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

print("Hello! Let's create a secure password.")
password_length = int(input("How long would you like your password to be?\n"))

all_characters = letters + numbers + symbols

password_list = [ ]
for char in range(password_length):
    password_list.append(random.choice(all_characters))

random.shuffle(password_list)
password = "".join(password_list)
print(f"Here is your password: {password}")


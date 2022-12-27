#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
rd_letters = ""
rd_letter = ""
rd_symbol = ""
rd_symbols = ""
rd_number = ""
rd_numbers = ""
for nr_letter in range (0,nr_letters):
  rd_chooser = random.randint(0,51)
  rd_letter = letters[rd_chooser]
  rd_letters += rd_letter
print(rd_letters)


for nr_symbol in range (0,nr_symbols):
  rd_chooser = random.randint(0,8)
  rd_symbol = symbols[rd_chooser]
  rd_symbols += rd_symbol
print(rd_symbols)
  
for nr_number in range (0,nr_numbers):
  rd_chooser = random.randint(0,9)
  rd_number = numbers[rd_chooser]
  rd_numbers += rd_number
print(rd_numbers)  

password = list(rd_letters+rd_symbols+rd_numbers)
print(type(password))
random.shuffle(password)
password_str=""
for passwords in password:
  password_str += passwords
print(password_str)

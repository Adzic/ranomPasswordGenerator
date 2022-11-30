#Random password generator made by Dimitrije on 11/30/2022
#Goal is to have a password that has letters, numbers, and symbols

import random
import string
import datetime
today = str(datetime.date.today())
print("Welcome to the random password generator!")

#Ask user for password length

length = int(input("How long do you want your password to be?"))

#Ask user for number of passwords

numPasswords = int(input("How many passwords do you want?"))

#Create a list of letters, numbers, and symbols

lettersLower = string.ascii_lowercase
lettersUpper = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

#Create a list of all the characters

all = lettersLower + lettersUpper + numbers + symbols

#Create a list of passwords

passwords = []

#Create a for loop to create the passwords

for i in range(numPasswords):
    password = "".join(random.sample(all, length))
    passwords.append(password)

#Print the passwords

for password in passwords:
    print(password)

#Save the passwords to a text file

with open("passwords-"+today+".txt", "w") as f:
    for password in passwords:
        f.write(password + "\n")



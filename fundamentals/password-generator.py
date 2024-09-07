import random
import string

password = []

raw_characters = string.ascii_letters, string.digits, string.punctuation # Using the string module to get all of the possible characters available
characters = list(''.join(raw_characters))

passwordLength = int(input("How many characters fo you want your password: "))

if passwordLength <= 7:
	print("Enter a number larger then 8")
	passwordLength = int(input("How many characters fo you want your password: "))

else:
	for length in range(passwordLength):
		selectedCharacter = random.choice(characters)
		password.append(selectedCharacter)
		
	print(f"Your password: {''.join(password)}")
import random


randomNumber = random.randint(0,100)
compleated = False

print("Guess the number between 0-100")

while compleated == False:
	guess = int(input("> "))

	if guess == randomNumber:
		print("Number guessed")
		quit()

	elif guess > randomNumber:
		print("Guess too high")

	elif guess < randomNumber:
		print("Guess too low")
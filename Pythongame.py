# Number guessing game
import random
a = input("Enter the guessed number between 0 to 10")
print("Your guessed number=",a)
c = (random.randint(0,10))
print("Computer guessed number=",c)
if a==c:
	print("Wow you guessed it right you won  ")
else:
	print("Oops its incorrect You lose ")



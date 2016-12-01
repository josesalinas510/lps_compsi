
# put this line at the start of your program
# to make the functions of this package available
import random
# creates a random number between 3 and 567 - edit as necessary
myNum = random.randint(1, 1000)

num = 0

print("Choose a number between 1 and 1000. Good luck")
while num < myNum:
	choice = int(raw_input())
	if choice < myNum:
		print("Choose a higher number")
	elif choice > myNum:
		print("Choose a lower number")
	elif choice == myNum:
		print("Nice job")
		num = 100000


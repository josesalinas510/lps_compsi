print("How many whole miles away from Richmond do you live?")
miles = int(raw_input())

print("What is your GPA?")
GPA = float(raw_input())

if miles < 30 and GPA >= 2.0:
	print("You're accepted")
elif miles > 30 and GPA >= 2.5:
	print("What is your ACT score?")
	ACT = int(raw_input())
	if ACT >= 18:
		print("You're accepted")
	else:
		print("Sorry, you do not meet the requirements")
else:
	print("Sorry, you do not meet the requirements")

        

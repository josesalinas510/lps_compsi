print("How many miles away from Richmond do you live?")
miles = int(raw_input()) 

print("What is your GPA?")
gpa = float(raw_input()) 

if miles > 30 and gpa < 2.5:
	print("Sorry, you were not accepted")

if miles < 30 and gpa < 2.0:
	print("Sorry, you were not accepted")

if miles > 30 and gpa >= 2.5 or miles < 30 and gpa >= 2.0:
	print("What is your ACT score?")
	act = int(raw_input()) 

gpa_2 = 2.0 - gpa
gpa_3 = 2.5 - gpa
act_2 = 18 - act

if miles < 30 and gpa >= 2.0 and act >= 18:
	print("You're accepted!")
elif miles > 30 and gpa < 2.5 and act < 18:
        print("You need " + str(gpa_3) + " points to meet the GPA requirement and " + str(act_2) + " points to meet the ACT requirement")
elif miles < 30 and gpa < 2.5 and act < 18:
        print("You need " + str(gpa_2) + " points to meet the GPA requirement and " + str(act_2) + " points to meet the ACT requirement")
elif miles > 30 and gpa >= 2.5 and act >= 18:
	print("You're accepted!")
elif miles < 30 and gpa < 2.0:
	print("You need to improve your GPA by " + str(gpa_2) + " to be accepted" )
elif miles < 30 and act < 18:
	print("You act score is " + str(act_2) + " points away, join the prep class!")
elif miles > 30 and gpa < 2.5:
	print("You need to improve your GPA by " + str(gpa_3))       
elif miles > 30 and act < 18:
	print("You act score is " + str(act_2) + " points away, join the prep class!")
else:
	print("Sorry, you were not accepted")




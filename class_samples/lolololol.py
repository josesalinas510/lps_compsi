print("How many miles away from Richmond State do you live?")
miles = int(raw_input())


print("What is your GPA?")
gpa = float(raw_input())


print("What is your ACT score?")
act = int(raw_input())


if miles < 30 and gpa >= 2.0 and act >= 18:
        print("You're accepted!")
elif miles > 30 and gpa >= 2.5 and act >= 18:
        print("You're accepted!")
else:
        print("Sorry, your scores do not meet the standard")


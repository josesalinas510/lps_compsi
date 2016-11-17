print("For what number would you like multiples of?")
num = int(raw_input())

count = 0
multiple = 0
while count < 1000:
	count = float(multiple * num)
	print(str(multiple) + " times " + str(num) + " equals " + str(count))
	multiple = multiple + 1
	
print("Those are all of the multiples up to 1000! Have a nice day!")

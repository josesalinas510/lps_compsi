# two variables, one for the the while statement and the other for an empty list
x = 0
y = []
while x < 5:
	print("What is your favorite show?")
	show = raw_input()
# for each input, the value of x is increased by 1. The loop will stop once x > 5
	x = x + 1
# each of the input is added onto the list
	y.append(show) 
print("Youre favorite shows are:" + str(y))


print("Here's a few more:")
# variable used to create a numerical list (not the coding type)
num = 1
y.append("The wire")
y.append("Breaking Bad")
y.sort()
for favs in y:
	print(str(num) + ". " + favs)
	num = num + 1
	


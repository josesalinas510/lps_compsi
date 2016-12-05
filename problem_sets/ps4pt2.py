x = 0
y = []
while x < 5:
	print("What is your favorite show?")
	show = raw_input()
	x = x + 1
	y.append(show) 
print("Youre favorite shows are:" + str(y))


print("Here's a few more:")
num = 1
y.append("The wire")
y.append("Breaking Bad")
for favs in y:
	print(str(num) + ". " + favs)
	num = num + 1
	


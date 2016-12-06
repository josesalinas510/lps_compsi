# two variables, one for the the while statement and the other for an empty list
x = 0
y = []

while x != "done":
	print("What are your favorite shows? Type in 'done' when you're finished") 
	show = raw_input()
# if the input is "done", then the loop ends	
	if show == "done":
        	x = "done"
	y.append(show) 
# the input "done" is removed from the list
y.remove("done")
print("Your favorite shows are:" + str(y))


print("Here's a few more:")
# variable used to create a numerical list (not the coding type)
num = 1
y.append("The wire")
y.append("Breaking Bad")
y.sort()
for favs in y:
	print(str(num) + ". " + favs)
	num = num + 1
	


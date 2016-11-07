print("How many people are at the party")
people = (raw_input())

print("How many donuts are there?")
donuts = int(raw_input())

print("There are " + str(donuts) + " donuts and " + str(people) + " people") 
amount = int(people) % int(donuts)
print("Each person gets " + str(amount) + " donut(s)")

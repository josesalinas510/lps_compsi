print('Pick a number from 1 to 25')
fave = int(17)
other_fave = int(raw_input())

if fave < other_fave:
	print("Sorry, try a lower number!")
if fave > other_fave:
	print("Sorry, try a higher number!")
if fave == other_fave:
	print("Hooray, you won! Good choice.")


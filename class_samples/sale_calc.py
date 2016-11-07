print("How much does this cost in cents?")

purchase = int(raw_input()) 

final_cost = float(purchase) * .1
if final_cost > 1000:
	print("You spent " + str(final_cost))





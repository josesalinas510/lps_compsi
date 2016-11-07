# Prompt asks for the user's input for their name and skill points
print("Welcome to Jose's Quest! Enter your character's name below")
name = raw_input()

print("You have 15 skill points to distribute among three skills. If you exceed the limit, all skills will be set to 5")

print("Enter strength (1-10)")
strength = int(raw_input())

print("Enter health (1-10)") 
health = int(raw_input())

print("Enter skill (1-10)")
luck = int(raw_input())

total_points = strength + health + luck
# this is to make sure that the user does not cheat and only uses the 15 points available 
if total_points > 15:
	print("You have used too many points, all stats were set to 5")
	strength = 5
	health = 5
	luck = 5
else:
	print("Your name is " + name + ", strength is " + str(strength) + ", health is " + str(health) + ", and your luck is " + str(luck)) 
# the game's story begins and the user's choice affects their outcome
print("You have been walking for ages with little water and almost no food. Your pack seems to feel heavier with each step. Upon reaching the river fork, you  have two options of going either left or right. What will you do?")

choice = raw_input()
#user can only pick left or right
if choice != "Left" and choice != "left" and choice != "Right" and choice != "right":
	print("Choose a proper direction")
# if they pick left, their outcome is decided by their stats
if choice == "left" or choice == "Left":
	print("The outside suddenly becomes dark and you are approached by a Giant")
elif choice == "left" or choice == "Left" and health > 4 and strength > 6:
        print("You were strong enough to slay the Giant and ran to safety!")
# if they pick right, their outcomes is decided by their stats
if choice == "right" or choice == "Right":
        print("There is a boat by the river bank. You boarded and sailed to a new life.")
elif choice == "right" or choice == "Right" and strength > 6 or luck > 8:
        print("A giant river monster attacked you while you were sailing home, but you were able to escape!")
else:
	print("You were not strong enough to defend yourself. Train more next time.")

print("Thank you for playing!")


# class type Player that holds multiple functions
class Player(object):
	""" Adds players and gives access to view the team """
	# function that contains variables that is unique to the input, meaning each input has its own name, age, and amount of goals
	def __init__(self, name, age, goals):
    		self.name = name
 		self.age = age
		self.goals = goals
# function that displays the player's name, age, and amount of goals
	def getStats(self):
		summary = "Player: " + self.name + "\n"
    		summary = summary + "Age: " + str(self.age) + "\n"
    		summary = summary + "Goals: " + str(self.goals) + "\n"
		return summary
	def saveTeam(playerList, filename):
		file = open("filename", "w")
		my_file = filename.write()
		file.close()

	def LoadTeam(self, List, filename):
		self.List = List
		self.filename = filename
		loadTeam = open("filename", "r")
		team = loadTeam.read()
		while team != "":
			details = team.split(" ")
			addPlayers.append(filename(details[0], details[1], details[2], details[3], details[4]))
			team = loadTeam.readline()
		loadTeam.close()

# execution starts here

# empty list that is used to add the players beng inputed 
myPlayers = []



keepRunning = True
print("Welcome to Team Manager Deluxe!")
print("Do you want to start with a new team or open an existing team?")
print("Enter the number of your choice and press enter")
print("(1) Start New Team")
print("(2) Add Existing Team")
print("(0) Exit.")
response = raw_input()

	
if response == "0":
	keepRunning = False

elif response == "1":
	option = yes
	print("Enter the number 0 when you finished adding all of the players.")
	print("To add another player, press any number besides 0")
       	while option == "yes" or option == "Yes":
		print("what is the player's name?")
       		playerName = raw_input()
       		print("What is the player's age?")
       		playerAge = int(raw_input())
       		print("How many goals have they scored?")
       		playerGoals = int(raw_input())
		print("What is their jersey number?")
		playerJersey = int(raw_input())
		print("What position do they play?")
		playerPosition = raw_input()
		newPlayer = Player(playerName, playerAge, playerGoals)
       		myPlayers.append(newPlayer)
       		print("Add another player? Enter Yes or No.")
		option = raw_input()
	for p in myPlayers:
    		print(p.getStats())

elif response == "2":
	print("What's the filename for your existing team? Enter the whole name, including its .tmd extension.")
	userFile = raw_input()
	for players in myPlayers:
		userFile.LoadTeam()
	
	print("What do you want to do? Enter the number of your choice and press Enter.")
	print("(1) Add a player")
	print("(2) Print all players")
	print("(3) Print average number of goals")
	print("(4) Save your player list to the file")
	print("(0) Leave the program (make sure to save first)")

		
	choice = raw_input()
	if choice == "1":
		print("Enter the number 0 when you finished adding all of the players.")
                print("To add another player, press any number besides 0")
                while option == "yes" or option == "Yes":
                        print("what is the player's name?")
                        playerName = raw_input()
                       	print("What is the player's age?")
                       	playerAge = int(raw_input())
                        print("How many goals have they scored?")
                        playerGoals = int(raw_input())
                        print("What is their jersey number?")
                        playerJersey = int(raw_input())
                        print("What position do they play?")
                        playerPosition = raw_input()
                        newPlayer = Player(playerName, playerAge, playerGoals)
                        myPlayers.append(newPlayer)
                        print("Add another player? Enter Yes or No.")
                        option = raw_input()

       	elif response == "2":
		for p in myPlayers:
                        print(p.getStats())
	elif response == "3":
		print("need to work on")

	elif response == "4":
		#saveTeam(userFile)
		pass

  
  
  
	

# class type Player that holds multiple functions
class Player(object):
	""" Adds players and gives access to view the team """
# function that contains variables that is unique to the input, meaning each input has its own name, age, and amount of goals
	def __init__(self, name, age, goals, jersNum, position):
    		self.name = name
 		self.age = age
		self.goals = goals
		self.jersNum = jersNum
		self.position = position
# function that displays the player's name, age, and amount of goals
	def getStats(self):
		summary = "Player: " + self.name + "\n"
    		summary = summary + "Age: " + str(self.age) + "\n"
    		summary = summary + "Goals: " + str(self.goals) + "\n"
		summary = summary + "Jersey: " + str(self.jersNum) + "\n"
		summary = summary + "Position: " + str(self.position) + "\n"
		return summary
# function to save team
def saveTeam(playerList, filename):
# opens the file
	existingFile = open(filename, "w")
# opens the file an input the information with a space in between	
	for players in existingFile:
		filename.write(player.name + " " + player.age + " " + player.goals + " " + player.jersNum + " " + player.position)
	filename.close()
# function that opens another file and splits the list containing the file's players info
def LoadTeam(myList, filename):
	loadTeam = open(filename, "r")
	team = loadTeam.read()
# splits the information into objects in a the list
	while team != "":
		details = team.split(" ")
		addPlayers.append(filename(details[0], details[1], details[2], details[3], details[4]))
		team = loadTeam.readline()
	loadTeam.close()

# execution starts here

# empty list that is used to add the players being inputed 
myPlayers = []
keepRunning = True
while keepRunning:
# prompts that enables the user to choos
	print("Welcome to Team Manager Deluxe!")
	print("Do you want to start with a new team or open an existing team?")
	print("Enter the number of your choice and press enter")
	print("(1) Start New Team")
	print("(2) Add Existing Team")
	print("(0) Exit.")
	response = raw_input()

# stops running the code	
	if response == "0":
		keepRunning = False
# option to make a new team if user inputs 1
	joseDaBest = True

	if response == "1":
		while joseDaBest:
			print("What do you want to do? Enter the number of your choice and press Enter.")
                	print("(1) Add a player")
                	print("(2) Print all players")
                	print("(3) Save your player list to the file")
                	print("(0) Leave the program (make sure to save first)")
			userOption = int(raw_input())
# user inputs the player's information
			if userOption == 1:
				print("Enter the player's information")     		
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
				newPlayer = Player(playerName, playerAge, playerGoals, playerJersey, playerPosition)
       				myPlayers.append(newPlayer)
       				print("Thank you")
			if userOption == 2:
				for players in myPlayers:
					print(players.getStats())
			if userOption == 0:
				break			
# displays the new players/info from the function getStats
	for p in myPlayers:
    		print(p.getStats())
# allows the user to input their own file with player info
	TeamLoading = True
	if response == "2":
		oldTeam = []
		print("What's the filename for your existing team? Enter the whole name, including its .tmd extension.")
		userFile = raw_input()
# loads in the the user's team
                LoadTeam(oldTeam, userFile)
		while TeamLoading:
			print("What do you want to do? Enter the number of your choice and press Enter.")
			print("(1) Add a player")
			print("(2) Print all players")
			print("(3) Save your player list to the file")
			print("(0) Leave the program (make sure to save first)")
			userChoice = int(raw_input())
			if userChoice == 1:
				print("Enter the player's information")
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
                                print("Thank you")
# shows all of the players and their information
			if userChoice == 2:
				for players in myPlayers:	
					print(players.getStats())
# saves the user's progress manually
			if userChoice == 3:
				print("What would you like to call this file?")
				filename = raw_input() + ".tmd"
				saveTeam(myPlayers, filename)
# ends the program	
			if userChoice == 0:
				break	

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



# execution starts here

# empty list that is used to add the players beng inputed 
myPlayers = []



keepRunning = True
# while the code runs, the prompts below appear 
while keepRunning:
  print("What would you like to do? Enter your choice and press 'enter'.")
  print("(1) Add players.")
  print("(2) View team.")
  print("(0) Exit.")
  # the user's input is labeled as "response" in order to use their responses for other functions
  response = raw_input()
# user inputs "0", the code ends
  if response == "0":
    keepRunning = False
# if user inputs "1", then they are asked to input the new player's name, age, and score. Then the player's information is added to the empty list containing the team
  elif response == "1":
    print("what is the player's name?")
    playerName = raw_input()
    print("What is the player's age?")
    playerAge = int(raw_input())
    print("How many goals have they scored?")
    playerGoals = int(raw_input())
    newPlayer = Player(playerName, playerAge, playerGoals)
    myPlayers.append(newPlayer)
# if the user inputs "2", the list is accessed and a summary of each player is displayed
  elif response == "2":
        for p in myPlayers:
          print(p.getStats())
          

  
  
  
  

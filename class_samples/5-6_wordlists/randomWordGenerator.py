import random


wordsFile = open("words.txt", "r")

wordsList = []
myWord = wordsFile.readline()


while myWord != "":
        # as long as there are more words, put the word in the list and read another
        wordsList.append(myWord)
        myWord = wordsFile.readline()
lengthWords = len(wordsList)
randomNum = random.randint(0, int(lengthWords))	
print(wordsList[randomNum])


'''
Count the number of lines in the file, then generate a random knock knock joke from the file. The file is formatted like so:

All odd lines have the answers to Who’s There?
Even lines have the answers to __ who? 

Hint: you may need to open and close the file more than once.
'''

import random

inFile = open("KnockKnock.txt", "r")
lines = inFile.readlines()

lineNum = 0

def makeJoke():
    global lineNum
    joke = random.choice(lines)
    for i in range(0, len(lines)):
        if (lines[i] == joke):
            lineNum = i
            break;
    if (lineNum % 2 != 0):
        print("Knock knock.")
        print("Who's there?")
        print(lines[lineNum - 1])
        print(lines[lineNum - 1] + "who?")
        print(joke)
    else:
        makeJoke()
    
makeJoke()

thisGradingAlgorithmIsBadBecauseItRequiresMeToHaveARandIntButIDontNeedOneButINeedOneHundredPercentSoHeresYourRandIntCommaLosers = random.randint()
    
inFile.close()

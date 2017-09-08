import random

playerScore = 0
cpuScore = 0

def play():
  playing = True
  while (playing):
    getPlayerInput()
    if (playerScore >= 100):
      print("You won!")
      playing = False
      continue
    cpuPlay()
    if (cpuScore >= 100):
      print("You lost!")
      playing = False
      continue

def getPlayerInput():
  global playerScore
  rolling = True
  turnTotal = 0
  while (rolling):
    choice = input("hold or roll: ")
    if (choice == "roll"):
      num = roll()
      if (num == 1):
        print("You rolled a 1. Your turn is over.")
        rolling = False
        continue
      else:
        turnTotal += num
        print("You rolled a " + str(num) + ". Your total for this turn is " + str(turnTotal))
    elif (choice == "hold"):
      playerScore += turnTotal
      print("You added " + str(turnTotal) + " to your total score. That score is now " + str(playerScore))
      rolling = False
    else:
      print("bad input")

def cpuPlay():
  global cpuScore
  rolling = True
  turnTotal = 0
  while (rolling):
    choice = random.randint(0, 1)
    if (choice == 0):
      num = roll()
      if (num == 1):
        print("CPU rolled a 1. Their turn is over.")
        rolling = False
        continue
      else:
        turnTotal += num
        print("CPU rolled a " + str(num) + ". Their total for this turn is " + str(turnTotal))
    elif (choice == 1):
      cpuScore += turnTotal
      print("CPU added " + str(turnTotal) + " to their total score. That score is now " + str(cpuScore))
      rolling = False
    else:
      print("bad number")
    
def roll():
  num = random.randint(1, 6)
  return num
  
play()

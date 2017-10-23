gameMap = None
currTurn = None
changeTurn = None
turnNum = None
playing = None

def main():
  global gameMap
  global currTurn
  global changeTurn
  global turnNum
  global playing
  gameMap = [["_" for i in range(3)] for j in range(3)]
  currTurn = "O"
  changeTurn = True
  turnNum = 0
  # main game loop
  playing = True
  while (playing):
    turnNum += 1
    print("=====================")
    print("|      Turn #" + str(turnNum) + "      |")
    print("|  Player " + currTurn + "'s turn  |")
    print("-===================-")
    printMap(gameMap)
    getUserInput(gameMap)
    if (changeTurn == True):
      if (currTurn == "X"):
        currTurn = "O"
        changeTurn = False
      else:
        currTurn = "X"
        changeTurn = False

# print game map
def printMap(map):
  print("|---- 1 - 2 - 3 ----|")
  for y in range(3):
    print("| " + str(y + 1), end="")
    for x in range(3):
      if (x == 0):
        print(" | " + map[x][y] + " | ", end="")
      elif (x == 2):
        print(" " + map[x][y] + " |   |", end="")
      else: 
        print(map[x][y] + " |", end="")
    print("\n|    -----------    |",)
  print("-===================-")

# get user input of column and row
def getUserInput(map):
  global currTurn
  global changeTurn
  global playing
  try:
    colChoice = int(input("Enter a COLUMN: "))
    if (colChoice > 3 or colChoice < 1):
      raise ValueError("Error: Column choice MUST be between 1 and 3")
    else:
      try:
        rowChoice = int(input("Enter a ROW: "))
        if (rowChoice > 3 or rowChoice < 1):
          raise ValueError("Error: Row choice MUST be between 1 and 3")
        else:
          try:
            if (map[colChoice - 1][rowChoice - 1] == "_"):
              map[colChoice - 1][rowChoice - 1] = currTurn
              if (checkVictory(map, colChoice - 1, rowChoice - 1)):
                printMap(map)
                print("=====================")
                print("PLAYER " + currTurn + " HAS WON!")
                print("=====================")
                playing = False
                changeTurn = False
              else:
                changeTurn = True
            else:
              raise ValueError("Error: Position already taken by player " + map[colChoice - 1][rowChoice - 1])
          except ValueError as err:
            print(err)
            changeTurn = False
      except ValueError as err:
        changeTurn = False
        if (err != "Error: Row choice MUST be between 1 and 3"):
          print(err)
        else:
          print("Error: Row choice not a number")
  except ValueError as err:
    changeTurn = False
    if (err != "Error: Column choice MUST be between 1 and 3"):
      print("Error: Column choice not a number")
    else:
      print(err)

def checkVictory(map, x, y):
  # vertical
  if map[0][y] == map[1][y] == map[2][y]:
    return True

  # horizontal
  if map[x][0] == map[x][1] == board [x][2]:
    return True

  # diagnal #1
  if x == y and map[0][0] == map[1][1] == map[2][2]:
    return True

  # diagnal #2
  if x + y == 2 and map[0][2] == map[1][1] == map[2][0]:
    return True
    
    return False  

main()

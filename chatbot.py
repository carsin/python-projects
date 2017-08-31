import random

running = False

def getName():
    return input("What is your name? ")

def getAge():
    return int(input("How old are you? "))

def getMood(name):
    mood = input("How are you? ")
    if (mood == "bad" or mood == "not good" or mood == "awful" or mood == "horrible"):
        getRandomResponse("bad")
        print("I'll leave you alone. Goodbye, feel better, " + name + ".")
        running = False
    else:
        getRandomResponse("good")

def getJob():
    return input("What do you do for a living? ")

def getMarriage():
    return input("Are you married? ")

def getRandomResponse(badOrGood):
    if (badOrGood == "bad"):
        print(badResponses[random.randint(0, len(badResponses))])
    elif (badOrGood == "good"):
        print(goodResponses[random.randint(0, len(goodResponses))])
    else:
        print("Bad input")

randQuestions = [
    getMood,
    getJob,
    getMarriage,
    "Do you go to school?",
]

goodResponses = [
    "Great!",
    "Good to hear.",
]

badResponses = [
    "Sorry.",
    "Sorry to hear that.",
    "Uh oh.",
    "Awww. Sorry."
]

def run():
    print("Hello!")
    running = True
    while running:
        


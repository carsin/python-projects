import random

name = "Unknown"
age = 0

def getName():
    name = input("What is your name? ")
    print("Nice to meet you, " + name)
    getAge(name)

def getAge(name):
    age = int(input("How old are you? "))
    print("Ah, so you're " + str(age) + ".")
    getMood(name, age)

def getMood(name, age):
    mood = str.lower(input("How are you? "))
    if (mood == "bad" or mood == "not good" or mood == "awful" or mood == "horrible"):
        getRandomResponse("bad")
        print("I'll leave you alone. Goodbye, feel better, " + name + ".")
    else:
        getRandomResponse("good")
        randNum = random.randint(0, 1)
        if (randNum == 0):
            getJob(name, age)
        elif (randNum == 1):
            getMarriage(name)
        else:
            print("Bad random number. Stopping.")

def getJob(name, age):
    job = str(input("So, " + name + " what does a man of " + str(age) + " years old do for a living? "))
    if (str.lower(job) == "nothing" or str.lower(job) == "unemployed" or str.lower(job) == "im not working" or str.lower(job) == "i'm not working" or str.lower(job) == "i'm unemployed" or str.lower(job) == "im unemployed"):
        getRandomResponse("bad")
    elif (str.lower(job) == "college" or str.lower(job) == "i go to college" or str.lower(job) == "school" or str.lower(job) == "i go to school" or str.lower(job) == "i'm in school" or str.lower(job) == "i go to university"):
        getRandomResponse("good")
        getSchooling(name, age)
    else:
        print("Interesting. " + job + " is a good job for you, " + name + ".")
        getMarriage(name)

def getMarriage(name):
    marriage = input("Are you married? ")
    if (str.lower(marriage) == "no" or str.lower(marriage) == "not yet" or str.lower(marriage) == "nope"):
        getRandomResponse("bad")
        goodbye(name)
    else:
        getRandomResponse("good")
        goodbye(name)

def getSchooling(name, age):
    if (age < 18):
        grade = int(input("What grade are you in " + name + "?"))
        randNum2 = random.randint(0, 1)
        if (randNum2 == 0):
            print("Ugh. I hated grade" + grade + "!")
        elif (randNum2 == 1):
            print("Cool! I loved grade" + grade + "!")
        else:
            print("Bad random number. Stopping.")
    else:
        major = str(input("What grade are you in " + name + "?"))
        if (str.lower(major) == "art"):
            getRandomResponse("bad")
        else:
            getRandomResponse("good")
    goodbye(name)

def goodbye(name):
    print("Well " + name + ", it has been nice talking to you.")

def getRandomResponse(badOrGood):
    if (badOrGood == "bad"):
        print(badResponses[random.randint(0, len(badResponses) - 1)])
    elif (badOrGood == "good"):
        print(goodResponses[random.randint(0, len(goodResponses) - 1)])
    else:
        print("Bad input")

goodResponses = [ "Great!", "Good to hear.", "Groovy!", "Excellent.", "Cool!", "Cool.", "Epic.", ]

badResponses = [ "Sorry.", "Sorry to hear that.", "Uh oh.", "Awww. Sorry.", "Damn.", "Darn.", "Crap.", "Uh oh.", ]

def start():
    print("Hello!")
    getName()
    
start()

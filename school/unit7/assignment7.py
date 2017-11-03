'''
In this assignment, you will write a program that will process data in the jokes.txt and answers.txt files.  Set up your program so that it will do the following tasks:

1) Display the number of jokes in jokes.txt
2) Ask the user for the number of a joke
3) Display the joke 
3) Display the requested joke 
4) Display the requested answer

'''

import random

jokeFile = open("jokes.txt", "r")
answerFile = open("answers.txt", "r")
allJokes = jokeFile.readlines()
allAnswers = answerFile.readlines()

def main():
    print(str(len(allJokes)) + " Jokes In File.")
    jokeChoice = int(input("Enter the number of the joke you want to hear: "))
    print("Joke #" + str(jokeChoice))
    print(allJokes[jokeChoice - 1])
    print(allAnswers[jokeChoice - 1])
main()
    
jokeFile.close()
answerFile.close()

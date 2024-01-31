import random

#variables
computerNum = 0
playerNum = 0
playerName = ""
guessCounter = 0
minNum = 0
maxNum = 0

print("The Number Guessing Number")

#get the range
print("Enter the minimum number?")
minNum = int(input())

print("Enter the maximum number?")
maxNum = int(input())

print("The computer has choice a random number between",minNum,"and",maxNum,", you goal to guess this number in the lowest number of attempts.")

#get player name
print("Enter your username?")
playerName = input()

#gens a random number bewteen user choice
computerNum = random.randrange(minNum,maxNum)

#start while loop
while playerNum != computerNum:
    #get players guess
    print("Enter your guess")
    playerNum = int(input())

    #add 1 to the counter
    guessCounter = guessCounter + 1

    #if the guess lower, give hint
    if int(playerNum) < int(computerNum):
        print("Try Higher")
        print("")

    #if the guess higher, give hint
    if int(playerNum) > int(computerNum):
        print("Try Lower")
        print("")

    #if guess matches, break out of the loop
    if int(playerNum) == int(computerNum):
        break

#display end message
print("")
print("Computer's number was", computerNum)
print(playerName ,"number of attempts is", guessCounter)
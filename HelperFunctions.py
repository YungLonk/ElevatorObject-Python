# Modules
from time import sleep
from re import search

# Describes how to use the program
def howToUse():
    print("Enter the floor you need when prompted.")
    print("If you need more floors, hit 'ctrl + c', and enter when prompted. Repeat up to 3 times.")
    print("")

# Prints user input error message
def userError():
    print("Enter either a floor number (1 - 5) or 'quit'.")
    print("")

# Closes the door
def closeDoor(sec=2):
    if sec == 2:
        print("Closing doors...")
        sleep(2)
    else: # Overload: This part can be interrupted
        print(f"Closing doors in {sec} seconds...")
        sleep(sec)

# Opens the door
def openDoor(currentFloor):
    print(f"Arrived at floor {currentFloor}; Opening doors...")
    sleep(4)

# Picks up the person
def pickUp(currentFloor):
    print(f"Picked up person from {currentFloor}.")
    sleep(1)

# Makes sure the number provided is anywhere from 1 to 5 (inclusive)
def isValidFloor(floorNum):
    if floorNum < 1 or floorNum > 5:
        return False
    else:
        return True

# Makes sure the word provided is the word "quit"
def isValidWord(word):
    if word != "quit":
        return False
    else:
        return True

# Makes sure input is a number
def isValidNumber(num):
    if not int(num):
        return False
    else:
        return True

# Runs user input through all validation
def isValidUserInput(userInput):
    if not isValidWord(userInput):
        hasLetters = search("[A-Za-z]", userInput)
        if hasLetters:
            return False
        elif userInput == "":
            return True
        else:
            intInput = int(userInput)
            if not isValidFloor(intInput):
                return False
            else:
                return True
    else:
        return True

# Returns the number of the requested floor (not floor 1, rather the floor requested 1st)
# Returns 0 if something went wrong
def closestNum(floorNeededDis, floorNeeded2Dis, *floorsNeededDis):
    oneTwo = floorNeededDis < floorNeeded2Dis
    match len(floorsNeededDis):
        #// 2 floors \\#
        case 0:
            if oneTwo:
                return 1
            elif not oneTwo:
                return 2
            else: return 0

        #// 3 floors \\#
        case 1:
            oneThree = floorNeededDis < floorsNeededDis[0]
            twoThree = floorNeeded2Dis < floorsNeededDis[0]
            if oneTwo and oneThree:
                return 1
            elif (not oneTwo) and twoThree:
                return 2
            elif (not oneThree) and (not twoThree):
                return 3
            else: return 0

        #// 4 floors \\#
        case 2:
            oneThree = floorNeededDis < floorsNeededDis[0]
            oneFour = floorNeededDis < floorsNeededDis[1]
            twoThree = floorNeeded2Dis < floorsNeededDis[0]
            twoFour = floorNeeded2Dis < floorsNeededDis[1]
            threeFour = floorsNeededDis[0] < floorsNeededDis[1]
            if oneTwo and oneThree and oneFour:
                return 1
            elif (not oneTwo) and twoThree and twoFour:
                return 2
            elif (not oneThree) and (not twoThree) and threeFour:
                return 3
            elif (not oneFour) and (not twoFour) and (not threeFour):
                return 4
            else: return 0
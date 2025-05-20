from HelperFunctions import *
from time import sleep

class Elvtr:
    def __init__(self):
        self.currentFloor = 1

    def getCurrentFloor(self):
        return self.currentFloor
    
    def setCurrentFloor(self, currentFloor):
        self.currentFloor = currentFloor

    # ---------------------------- Processing Methods ---------------------------- #
    # ----- Returns false if the requested floors are not in opposite directions ----- #
    def areOppositeDirections(self, floorNeeded, floorNeeded2, *floorsNeeded):
        # Position of 1st and 2nd floors needed relative to currentFloor
        currentFloor = self.currentFloor # Shorthand for self.currentFloor; this function doesn't change currentFloor
        current1Dif = currentFloor - floorNeeded
        current2Dif = currentFloor - floorNeeded2
        below1 = current1Dif < 0
        above1 = current1Dif > 0
        below2 = current2Dif < 0
        above2 = current2Dif > 0
        match len(floorsNeeded):
            #// 2 floors \\#
            case 0:
                abv1Blw2 = above1 and below2
                blw1Abv2 = below1 and above2
                if (not abv1Blw2) and (not blw1Abv2): # If both floors either above or below current floor
                    return False
                else: return True

            #// 3 floors \\#
            case 1:
                # Position of 3rd floor needed relative to currentFloor
                current3Dif = currentFloor - floorsNeeded[0]
                below3 = current3Dif < 0
                above3 = current3Dif > 0
                blw1Blw2Abv3 = below1 and below2 and above3
                blw1Abv2Blw3 = below1 and above2 and below3
                abv1Blw2Blw3 = above1 and below2 and below3
                blw1Abv2Abv3 = below1 and above2 and above3
                abv1Abv2Blw3 = above1 and above2 and below3
                abv1Blw2Abv3 = above1 and below2 and above3
                blwOrAbove1 = (not blw1Blw2Abv3) and (not blw1Abv2Blw3) and (not abv1Blw2Blw3)
                blwOrAbove2 = (not blw1Abv2Abv3) and (not abv1Abv2Blw3) and (not abv1Blw2Abv3)
                if blwOrAbove1 and blwOrAbove2: # If all floors either above or below current floor
                    return False
                else: return True

            #// 4 floors \\#
            case 2:
                # Position of 3rd and 4th floor needed relative to currentFloor
                current3Dif = currentFloor - floorsNeeded[0]
                current4Dif = currentFloor - floorsNeeded[1]
                below3 = current3Dif < 0
                above3 = current3Dif > 0
                below4 = current4Dif < 0
                above4 = current4Dif > 0
                # All possible outcomes
                blw1Blw2Blw3Abv4 = below1 and below2 and below3 and above4
                blw1Blw2Abv3Blw4 = below1 and below2 and above3 and below4
                blw1Abv2Blw3Blw4 = below1 and above2 and below3 and below4
                abv1Blw2Blw3Blw4 = above1 and below2 and below3 and below4
                blw1Blw2Abv3Abv4 = below1 and below2 and above3 and above4
                blw1Abv2Abv3Blw4 = below1 and above2 and above3 and below4
                abv1Abv2Blw3Blw4 = above1 and above2 and below3 and below4
                blw1Abv2Blw3Abv4 = below1 and above2 and below3 and above4
                abv1Blw2Blw3Abv4 = above1 and below2 and below3 and above4
                abv1Blw2Abv3Blw4 = above1 and below2 and above3 and below4
                blw1Abv2Abv3Abv4 = below1 and above2 and above3 and above4
                abv1Blw2Abv3Abv4 = above1 and below2 and above3 and above4
                abv1Abv2Blw3Abv4 = above1 and above2 and below3 and above4
                abv1Abv2Abv3Blw4 = above1 and above2 and above3 and below4
                # If all floors either above or below current floor
                blwOrAbove1 = (blw1Blw2Blw3Abv4) and (blw1Blw2Abv3Blw4) and (blw1Abv2Blw3Blw4) and (abv1Blw2Blw3Blw4)
                blwOrAbove2 = (blw1Blw2Abv3Abv4) and (blw1Abv2Abv3Blw4) and (abv1Abv2Blw3Blw4)
                blwOrAbove3 = (blw1Abv2Blw3Abv4) and (abv1Blw2Blw3Abv4) and (abv1Blw2Abv3Blw4)
                blwOrAbove4 = (blw1Abv2Abv3Abv4) and (abv1Blw2Abv3Abv4) and (abv1Abv2Blw3Abv4) and (abv1Abv2Abv3Blw4)
                if blwOrAbove1 and blwOrAbove2 and blwOrAbove3 and blwOrAbove4:
                    return False
                else: return True

    # ----- Returns tuple of floors ordered in closeness to currentFloor ----- #
    def closestFloor(self, floorNeeded, floorNeeded2, *floorsNeeded):
        # Relational data
        currentFloor = self.currentFloor
        current1Dif = currentFloor - floorNeeded #  These two will be used when
        current2Dif = currentFloor - floorNeeded2 # they're both below currentFloor...
        oneCurrentDif = floorNeeded - currentFloor #  ... and these two will be used when
        twoCurrentDif = floorNeeded2 - currentFloor # they're both above currentFloor
        below1 = current1Dif < 0
        above1 = current1Dif > 0
        below2 = current2Dif < 0
        above2 = current2Dif > 0

        # Actual determination (if anything goes wrong, returns tuple (0))
        match len(floorsNeeded):
            #// 2 floors \\#
            case 0:
                if below1 and below2: # If currentFloor below both floors
                    match(closestNum(oneCurrentDif, twoCurrentDif)):
                        case 1: return (floorNeeded, floorNeeded2)
                        case 2: return (floorNeeded2, floorNeeded)
                        case _: return (0) # If something goes wrong, retuns tuple with int 0 at index 0
                
                elif above1 and above2: # If currentFloor above both floors
                    match(closestNum(current1Dif, current2Dif)):
                        case 1: return (floorNeeded, floorNeeded2)
                        case 2: return (floorNeeded2, floorNeeded)
                        case _: return (0) # If something goes wrong, returns tuple with int 0 at index 0
            
            #// 3 floors \\#
            case 1:
                floorNeeded3 = floorsNeeded[0]
                current3Dif = currentFloor - floorNeeded3
                current3Dif = floorNeeded3 - currentFloor
                below3 = current3Dif < 0
                above3 = current3Dif > 0
                if below1 and below2 and below3: # If currentFloor below all needed floors
                    match(closestNum(oneCurrentDif, twoCurrentDif, threeCurrentDif)):
                        case 1: # (floorNeeded, x, x)
                            match(closestNum(twoCurrentDif, threeCurrentDif)):
                                case 1: return (floorNeeded, floorNeeded2, floorNeeded3)
                                case 2: return (floorNeeded, floorNeeded3, floorNeeded2)
                                case _: return (0)

                        case 2:  # (floorNeeded2, x, x)
                            match(closestNum(oneCurrentDif, threeCurrentDif)):
                                case 1: return (floorNeeded2, floorNeeded, floorNeeded3)
                                case 2: return (floorNeeded2, floorNeeded3, floorNeeded)
                                case _: return (0)

                        case 3: # (floorNeeded3, x, x)
                            match(closestNum(oneCurrentDif, twoCurrentDif)):
                                case 1: return (floorNeeded3, floorNeeded, floorNeeded2)
                                case 2: return (floorNeeded3, floorNeeded2, floorNeeded)
                                case _: return (0)
                        case _: return (0)
                
                elif above1 and above2 and above3: # If currentFloor above all needed floors
                    match(closestNum(current1Dif, current2Dif, current3Dif)):
                        case 1: # (floorNeeded, x, x)
                            match(closestNum(current2Dif, current3Dif)):
                                case 1: return (floorNeeded, floorNeeded2, floorNeeded3)
                                case 2: return (floorNeeded, floorNeeded3, floorNeeded2)
                                case _: return (0)
                        case 2: # (floorNeeded2, x, x)
                            match(closestNum(current1Dif, current3Dif)):
                                case 1: return (floorNeeded2, floorNeeded, floorNeeded3)
                                case 2: return (floorNeeded2, floorNeeded3, floorNeeded)
                                case _: return (0)
                        case 3: # (floorNeeded3, x, x)
                            match(closestNum(current1Dif, current2Dif)):
                                case 1: return (floorNeeded3, floorNeeded, floorNeeded2)
                                case 2: return (floorNeeded3, floorNeeded2, floorNeeded)
                                case _: return (0)
                        case _: return (0)

            #// 4 floors \\#
            case 2:
                floorNeeded3 = floorsNeeded[0]
                floorNeeded4 = floorsNeeded[1]
                current3Dif = currentFloor - floorNeeded3
                current4Dif = currentFloor - floorNeeded4
                threeCurrentDif = floorNeeded3 - currentFloor
                fourCurrentDif = floorNeeded4 - currentFloor
                below3 = current3Dif < 0
                above3 = current3Dif > 0
                below4 = current4Dif < 0
                above4 = current4Dif > 0
                if below1 and below2 and below3 and below4: # If currentFloor below all needed floors
                    match(closestNum(oneCurrentDif, twoCurrentDif, threeCurrentDif, fourCurrentDif)):
                        case 1: # (floorNeeded, x, x, x)
                            match(closestNum(twoCurrentDif, threeCurrentDif, fourCurrentDif)):
                                case 1: # (floorNeeded, floorNeeded2, x, x)
                                    match(closestNum(threeCurrentDif, fourCurrentDif)):
                                        case 1: return (floorNeeded, floorNeeded2, floorNeeded3, floorNeeded4)
                                        case 2: return (floorNeeded, floorNeeded2, floorNeeded4, floorNeeded3)
                                        case _: return (0)

                                case 2: # (floorNeeded, floorNeeded3, x, x)
                                    match(closestNum(twoCurrentDif, fourCurrentDif)):
                                        case 1: return (floorNeeded, floorNeeded3, floorNeeded2, floorNeeded4)
                                        case 2: return (floorNeeded, floorNeeded3, floorNeeded4, floorNeeded2)
                                        case _: return (0)

                                case 3: # (floorNeeded, floorNeeded4, x, x)
                                    match(closestNum(twoCurrentDif, threeCurrentDif)):
                                        case 1: return (floorNeeded, floorNeeded4, floorNeeded2, floorNeeded3)
                                        case 2: return (floorNeeded, floorNeeded4, floorNeeded3, floorNeeded2)
                                        case _: return (0)
                                case _: return (0)

                        case 2: # (floorNeeded2, x, x, x)
                            match(closestNum(oneCurrentDif, threeCurrentDif, fourCurrentDif)):
                                case 1: # (floorNeeded2, floorNeeded, x, x)
                                    match(closestNum(threeCurrentDif, fourCurrentDif)):
                                        case 1: return (floorNeeded2, floorNeeded, floorNeeded3, floorNeeded4)
                                        case 2: return (floorNeeded2, floorNeeded, floorNeeded4, floorNeeded3)
                                        case _: return (0)
                                
                                case 2: # (floorNeeded2, floorNeeded3, x, x)
                                    match(closestNum(oneCurrentDif, fourCurrentDif)):
                                        case 1: return (floorNeeded2, floorNeeded3, floorNeeded, floorNeeded4)
                                        case 2: return (floorNeeded2, floorNeeded3, floorNeeded4, floorNeeded)
                                        case _: return (0)

                                case 3: # (floorNeeded2, floorNeeded4, x, x)
                                    match(closestNum(oneCurrentDif, threeCurrentDif)):
                                        case 1: return (floorNeeded2, floorNeeded4, floorNeeded, floorNeeded3)
                                        case 2: return (floorNeeded2, floorNeeded4, floorNeeded3, floorNeeded)
                                        case _: return (0)
                                case _: return (0)

                        case 3: # (floorNeeded3, x, x, x)
                            match(closestNum(oneCurrentDif, twoCurrentDif, fourCurrentDif)):
                                case 1: # (floorNeeded3, floorNeeded, x, x)
                                    match(closestNum(twoCurrentDif, fourCurrentDif)):
                                        case 1: return (floorNeeded3, floorNeeded, floorNeeded2, floorNeeded4)
                                        case 2: return (floorNeeded3, floorNeeded, floorNeeded4, floorNeeded3)
                                        case _: return (0)

                                case 2: # (floorNeeded3, floorNeeded2, x, x)
                                    match(closestNum(oneCurrentDif, fourCurrentDif)):
                                        case 1: return (floorNeeded3, floorNeeded2, floorNeeded, floorNeeded4)
                                        case 2: return (floorNeeded3, floorNeeded2, floorNeeded4, floorNeeded)
                                        case _: return (0)

                                case 3: # (floorNeeded3, floorNeeded4, x, x)
                                    match(closestNum(oneCurrentDif, twoCurrentDif)):
                                        case 1: return (floorNeeded3, floorNeeded4, floorNeeded, floorNeeded2)
                                        case 2: return (floorNeeded3, floorNeeded4, floorNeeded2, floorNeeded)
                                        case _: return (0)
                                case _: return (0)
                        
                        case 4: # (floorNeeded4, x, x, x)
                            match(closestNum(oneCurrentDif, twoCurrentDif, threeCurrentDif)):
                                case 1: # (floorNeeded4, floorNeeded, x, x)
                                    match(closestNum(twoCurrentDif, threeCurrentDif)):
                                        case 1: return (floorNeeded4, floorNeeded, floorNeeded2, floorNeeded3)
                                        case 2: return (floorNeeded4, floorNeeded, floorNeeded3, floorNeeded2)
                                        case _: return (0)

                                case 2: # (floorNeeded4, floorNeeded2, x, x)
                                    match(closestNum(oneCurrentDif, threeCurrentDif)):
                                        case 1: return (floorNeeded4, floorNeeded2, floorNeeded, floorNeeded3)
                                        case 2: return (floorNeeded4, floorNeeded2, floorNeeded3, floorNeeded)
                                        case _: return (0)

                                case 3: # (floorNeeded4, floorNeeded3, x, x)
                                    match(closestNum(oneCurrentDif, twoCurrentDif)):
                                        case 1: return (floorNeeded4, floorNeeded3, floorNeeded, floorNeeded2)
                                        case 2: return (floorNeeded4, floorNeeded3, floorNeeded2, floorNeeded)
                                        case _: return (0)
                                case _: return (0)
                        case _: return (0)
                
                elif above1 and above2 and above3 and above4: # If current floor above all other floors
                    match(closestNum(current1Dif, current2Dif, current3Dif, current4Dif)):
                        case 1: # (floorNeeded, x, x, x)
                            match(closestNum(current2Dif, current3Dif, current4Dif)):
                                case 1: # (floorNeeded, floorNeeded2, x, x)
                                    match(closestNum(current3Dif, current4Dif)):
                                        case 1: return (floorNeeded, floorNeeded2, floorNeeded3, floorNeeded4)
                                        case 2: return (floorNeeded, floorNeeded2, floorNeeded4, floorNeeded3)
                                        case _: return (0)

                                case 2: # (floorNeeded, floorNeeded3, x, x)
                                    match(closestNum(current2Dif, current4Dif)):
                                        case 1: return (floorNeeded, floorNeeded3, floorNeeded2, floorNeeded4)
                                        case 2: return (floorNeeded, floorNeeded3, floorNeeded4, floorNeeded2)
                                        case _: return (0)

                                case 3: # (floorNeeded, floorNeeded4, x, x)
                                    match(closestNum(current2Dif, current3Dif)):
                                        case 1: return (floorNeeded, floorNeeded4, floorNeeded2, floorNeeded3)
                                        case 2: return (floorNeeded, floorNeeded4, floorNeeded3, floorNeeded2)
                                        case _: return (0)
                                case _: return (0)

                        case 2: # (floorNeeded2, x, x, x)
                            match(closestNum(current1Dif, current3Dif, current4Dif)):
                                case 1: # (floorNeeded2, floorNeeded, x, x)
                                    match(closestNum(current3Dif, current4Dif)):
                                        case 1: return (floorNeeded2, floorNeeded, floorNeeded3, floorNeeded4)
                                        case 2: return (floorNeeded2, floorNeeded, floorNeeded4, floorNeeded3)
                                        case _: return (0)
                                
                                case 2: # (floorNeeded2, floorNeeded3, x, x)
                                    match(closestNum(current1Dif, current4Dif)):
                                        case 1: return (floorNeeded2, floorNeeded3, floorNeeded, floorNeeded4)
                                        case 2: return (floorNeeded2, floorNeeded3, floorNeeded4, floorNeeded)
                                        case _: return (0)

                                case 3: # (floorNeeded2, floorNeeded4, x, x)
                                    match(closestNum(current1Dif, current3Dif)):
                                        case 1: return (floorNeeded2, floorNeeded4, floorNeeded, floorNeeded3)
                                        case 2: return (floorNeeded2, floorNeeded4, floorNeeded3, floorNeeded)
                                        case _: return (0)
                                case _: return (0)

                        case 3: # (floorNeeded3, x, x, x)
                            match(closestNum(current1Dif, current2Dif, current4Dif)):
                                case 1: # (floorNeeded3, floorNeeded, x, x)
                                    match(closestNum(current2Dif, current4Dif)):
                                        case 1: return (floorNeeded3, floorNeeded, floorNeeded2, floorNeeded4)
                                        case 2: return (floorNeeded3, floorNeeded, floorNeeded4, floorNeeded3)
                                        case _: return (0)

                                case 2: # (floorNeeded3, floorNeeded2, x, x)
                                    match(closestNum(current1Dif, current4Dif)):
                                        case 1: return (floorNeeded3, floorNeeded2, floorNeeded, floorNeeded4)
                                        case 2: return (floorNeeded3, floorNeeded2, floorNeeded4, floorNeeded)
                                        case _: return (0)

                                case 3: # (floorNeeded3, floorNeeded4, x, x)
                                    match(closestNum(current1Dif, current2Dif)):
                                        case 1: return (floorNeeded3, floorNeeded4, floorNeeded, floorNeeded2)
                                        case 2: return (floorNeeded3, floorNeeded4, floorNeeded2, floorNeeded)
                                        case _: return (0)
                                case _: return (0)
                        
                        case 4: # (floorNeeded4, x, x, x)
                            match(closestNum(current1Dif, current2Dif, current3Dif)):
                                case 1: # (floorNeeded4, floorNeeded, x, x)
                                    match(closestNum(current2Dif, current3Dif)):
                                        case 1: return (floorNeeded4, floorNeeded, floorNeeded2, floorNeeded3)
                                        case 2: return (floorNeeded4, floorNeeded, floorNeeded3, floorNeeded2)
                                        case _: return (0)

                                case 2: # (floorNeeded4, floorNeeded2, x, x)
                                    match(closestNum(current1Dif, current3Dif)):
                                        case 1: return (floorNeeded4, floorNeeded2, floorNeeded, floorNeeded3)
                                        case 2: return (floorNeeded4, floorNeeded2, floorNeeded3, floorNeeded)
                                        case _: return (0)

                                case 3: # (floorNeeded4, floorNeeded3, x, x)
                                    match(closestNum(current1Dif, current2Dif)):
                                        case 1: return (floorNeeded4, floorNeeded3, floorNeeded, floorNeeded2)
                                        case 2: return (floorNeeded4, floorNeeded3, floorNeeded2, floorNeeded)
                                        case _: return (0)
                                case _: return (0)
                        case _: return (0)
    
    # Sends elevator to floor needed
    def switchingFloors(self, floorNeeded):
        while self.currentFloor < floorNeeded: # Current floor below floor needed. Go up.
            print(f"Currently at floor {self.currentFloor}. Going down...")
            sleep(5)
            self.currentFloor += 1
        else:
            while self.currentFloor > floorNeeded: # Current floor above floor needed. Go down.
                print(f"Currently at floor {self.currentFloor}. Going down...")
                sleep(5)
                self.currentFloor -= 1
    
    # Makes elevator move
    def execute(self, floorNeeded, floorsNeeded):
        # Always one floor needed
        closeDoor()
        self.switchingFloors(floorNeeded)
        openDoor(self.currentFloor)
        if len(floorsNeeded) > 0: # If other floors are also needed
            for i in range(len(floorsNeeded)):
                closeDoor()
                self.switchingFloors(floorsNeeded[i])
                openDoor(self.currentFloor)
    
    # Runs the execute function after sorting floors needed, going to each in sequential order
    def efficient(self, floorNeeded, floorNeeded2, floorsNeeded):
        match len(floorsNeeded):
            case 0: # 2 floors needed
                closest = self.closestFloor(floorNeeded, floorNeeded2)
                self.execute(closest[0], closest[1])
            case 1: # 3 floors needed
                closest = self.closestFloor(floorNeeded, floorNeeded2, floorsNeeded[0])
                self.execute(closest[0], closest[1], closest[2])
            case 2: # 4 floors needed
                closest = self.closestFloor(floorNeeded, floorNeeded2, floorsNeeded[0], floorsNeeded[1])
                self.execute(closest[0], closest[1], closest[2], closest[3])

    # Determines whether or not above function is needed (runs execute directly if not)
    def floorReq(self, floorNeeded, *floorsNeeded):
        match len(floorsNeeded):
            case 0: self.execute(floorNeeded) # 1 floor needed
            case 1: # 2 floors needed
                are = self.areOppositeDirections(floorNeeded, floorsNeeded[0])
                if not are: self.efficient(floorNeeded, floorsNeeded[0])
                else: self.execute(floorNeeded, floorsNeeded[0])
            case 2: # 3 floors needed
                are = self.areOppositeDirections(floorNeeded, floorsNeeded[0], floorsNeeded[1])
                if not are: self.efficient(floorNeeded, floorsNeeded[0])
                else: self.execute(floorNeeded, floorsNeeded[0], floorsNeeded[1])
            case 3: # 4 floors needed
                are = self.areOppositeDirections(floorNeeded, floorsNeeded[0], floorsNeeded[1], floorsNeeded[2])
                if not are: self.efficient(floorNeeded, floorsNeeded[0], floorsNeeded[1], floorsNeeded[2])
                else: self.execute(floorNeeded, floorsNeeded[0], floorsNeeded[1], floorsNeeded[2])

# -------------------- Main Function -------------------- #
def main():
    howToUse()
    el = Elvtr()
    keepGoing = True
    while keepGoing:
        floor = input("Which floor do you need?: ")
        if not isValidUserInput(floor):
            userError()
            keepGoing = True
            continue
        elif floor == 'quit':
            print("Elevator shutting down...")
            sleep(2)
            keepGoing = False
            continue
        else:
            floor2, floor3, floor4 = "", "", ""
            floors = [floor, floor2, floor3, floor4]
            intFloors = []
            for x in floors:
                x = input("Which floor do you need? (hit enter if all floors requested): ")
                while floor == 'quit':
                    print("You already requested a floor. You must enter more now")
                    print("")
                    x = input("Which floor do you need? (hit enter if all floors requested): ")
                while not isValidUserInput(x):
                    userError()
                    x = input("Which floor do you need? (hit enter if all floors requested): ")
            for i in range(3):
                if floors[i] != "":
                    intFloors[i] = int(floors[i])
            intLen = len(intFloors)
            if intLen == 1: el.floorReq(intFloors[0])
            elif intLen == 2: el.floorReq(intFloors[0], intFloors[1])
            elif intLen == 3: el.floorReq(intFloors[0], intFloors[1], intFloors[2])
            elif intLen == 4: el.floorReq(intFloors[0], intFloors[1], intFloors[2], intFloors[3])

if __name__ == '__main__':
    main()
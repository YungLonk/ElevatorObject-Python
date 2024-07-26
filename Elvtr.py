from HelperFunctions import *
from time import sleep

class Elvtr:
    def __init__(self):
        self.currentFloor = 1

    def getCurrentFloor(self):
        return self.currentFloor
    
    def setCurrentFloor(self, currentFloor):
        self.currentFloor = currentFloor
    
    # Checks for floors in opposite directions relative to currentFloor; passes along currentFloor
    def areOppositeDirections(self, currentFloor, floorNeeded, floorNeeded2, *floorsNeeded):
        match len(floorsNeeded):
            case 0: # 2 floors
                current1Dif = currentFloor - floorNeeded
                current2Dif = currentFloor - floorNeeded2
                below1 = current1Dif < 0
                above1 = current1Dif > 0
                below2 = current2Dif < 0
                above2 = current2Dif > 0
                a1B2 = above1 and below2
                b1A2 = below1 and above2
                if (not b1A2) and (not a1B2):
                    return False
                else:
                    return True
                
            case 1: # 3 floors
                current1Dif = currentFloor - floorNeeded
                current2Dif = currentFloor - floorNeeded2
                current3Dif = currentFloor - floorsNeeded[0]
                below1 = current1Dif < 0
                above1 = current1Dif > 0
                below2 = current2Dif < 0
                above2 = current2Dif > 0
                below3 = current3Dif < 0
                above3 = current3Dif > 0
                b1B2A3 = below1 and below2 and above3
                b1A2B3 = below1 and above2 and below3
                a1B2B3 = above1 and below2 and below3
                b1A2A3 = below1 and above2 and above3
                a1A2B3 = above1 and above2 and below3
                a1B2A3 = above1 and below2 and above3
                notBelowOrAbovePt1 = (not b1B2A3) and (not b1A2B3) and (not a1B2B3)
                notBelowOrAbovePt2 = (not b1A2A3) and (not a1A2B3) and (not a1B2A3)
                if notBelowOrAbovePt1 and notBelowOrAbovePt2:
                    return False
                else:
                    return True
                
            case 2: # 4 floors
                # Describe position of a floor relative to the currentFloor
                current1Dif = currentFloor - floorNeeded # Current floor above first floor needed
                current2Dif = currentFloor - floorNeeded2 # Current floor above second floor needed
                current3Dif = currentFloor - floorsNeeded[0] # Current floor above third floor needed
                current4Dif = currentFloor - floorsNeeded[1] # Current floor above fourth floor needed
                below1 = current1Dif < 0
                above1 = current1Dif > 0
                below2 = current2Dif < 0
                above2 = current2Dif > 0
                below3 = current3Dif < 0
                above3 = current3Dif > 0
                below4 = current4Dif < 0
                above4 = current4Dif > 0

                # 4-floor-request scenario possible outcomes (a = Above; b = Below)
                b1B2B3A4 = below1 and below2 and below3 and above4
                b1B2A3B4 = below1 and below2 and above3 and below4
                b1A2B3B4 = below1 and above2 and below3 and below4
                a1B2B3B4 = above1 and below2 and below3 and below4
                b1B2A3A4 = below1 and below2 and above3 and above4
                b1A2A3B4 = below1 and above2 and above3 and below4
                a1A2B3B4 = above1 and above2 and below3 and below4
                b1A2B3A4 = below1 and above2 and below3 and above4
                a1B2B3A4 = above1 and below2 and below3 and above4
                a1B2A3B4 = above1 and below2 and above3 and below4
                b1A2A3A4 = below1 and above2 and above3 and above4
                a1B2A3A4 = above1 and below2 and above3 and above4
                a1A2B3A4 = above1 and above2 and below3 and above4
                a1A2A3B4 = above1 and above2 and above3 and below4

                # Conditional statement
                allInLinePt1 = (not b1B2B3A4) and (not b1B2A3B4) and (not b1A2B3B4) and (not a1B2B3B4)
                allInLinePt2 = (not b1B2A3A4) and (not b1A2A3B4) and (not a1A2B3B4)
                allInLinePt3 = (not b1A2B3A4) and (not a1B2B3A4) and (not a1B2A3B4)
                allInLinePt4 = (not b1A2A3A4) and (not a1B2A3A4) and (not a1A2B3A4) and (not a1A2A3B4)
                if (allInLinePt1) and (allInLinePt2) and (allInLinePt3) and (allInLinePt4):
                    return False
                else:
                    return True
    
    # Returns tuple of floors in proximity order (closest, 2ndclosest, 3rdclosest, ...)
    def closestFloor(self, currentFloor, floorNeeded, floorNeeded2, *floorsNeeded):
        # Describe position of a floor relative to currentFloor #
        current1Dif = currentFloor - floorNeeded
        current2Dif = currentFloor - floorNeeded2
        oneCurrentDif = floorNeeded - currentFloor
        twoCurrentDif = floorNeeded2 - currentFloor
        below1 = current1Dif < 0
        above1 = current1Dif > 0
        below2 = current2Dif < 0
        above2 = current2Dif > 0

        match len(floorsNeeded):
            case 0: # 2 floors
                if below1 and below2:
                    oneCurrCloser = oneCurrentDif < twoCurrentDif
                    twoCurrCloser = oneCurrentDif > twoCurrentDif
                    if oneCurrCloser:
                        return (floorNeeded, floorNeeded2)
                    elif twoCurrCloser:
                        return (floorNeeded2, floorNeeded)
                elif above1 and above2:
                    oneCurrCloser = current1Dif < current2Dif
                    twoCurrCloser = current1Dif > current2Dif
                    if oneCurrCloser:
                        return (floorNeeded, floorNeeded2)
                    elif twoCurrCloser:
                        return (floorNeeded2, floorNeeded)
            
            case 1: # 3 floors
                floorNeeded3 = floorsNeeded[0]
                current3Dif = currentFloor - floorNeeded3
                threeCurrentDif = floorNeeded3 - currentFloor
                below3 = current1Dif < 0
                above3 = current1Dif > 0

                if below1 and below2 and below3:

                elif above1 and above2 and above3:

            case 2: # 4 floors

            case _:
                return ()
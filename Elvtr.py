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
    # ----- Returns whether or not the requested floors are in opposite directions ----- #
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
        currentFloor = self.currentFloor
        current1Dif = currentFloor - floorNeeded #  These two will be used when
        current2Dif = currentFloor - floorNeeded2 # they're both below currentFloor...
        oneCurrentDif = floorNeeded - currentFloor #  ... and these two will be used when
        twoCurrentDif = floorNeeded2 - currentFloor # they're both above currentFloor
        below1 = current1Dif < 0
        above1 = current1Dif > 0
        below2 = current2Dif < 0
        above2 = current2Dif > 0
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
                
                elif above1 and above2 and above3: # If currentFloor above all needed floors
                    match(closestNum(current1Dif, current2Dif, current3Dif)):
                        case 1:
                            twoCurrCloser = current2Dif < current3Dif
                            threeCurrCloser = current2Dif > current3Dif
                            if twoCurrCloser: # floorNeeded2 is next closest
                                return (floorNeeded, floorNeeded2, floorNeeded3)
                            elif threeCurrCloser: # floorNeeded3 is next closest
                                return (floorNeeded, floorNeeded3, floorNeeded2)
                        case 2:
                            oneCurrCloser = current1Dif < current3Dif
                            threeCurrCloser = current1Dif > current3Dif
                            if oneCurrCloser: # floorNeeded is next closest
                                return (floorNeeded2, floorNeeded, floorNeeded3)
                            elif threeCurrCloser: # floorNeeded3 is next closest
                                return (floorNeeded2, floorNeeded3, floorNeeded)
                        case 3:
                            oneCurrCloser = current1Dif < current2Dif
                            twoCurrCloser = current1Dif > current2Dif
                            if oneCurrCloser: # floorNeeded is next closest
                                return (floorNeeded3, floorNeeded, floorNeeded2)
                            elif twoCurrCloser: # floorNeeded2 is next closest
                                return (floorNeeded3, floorNeeded2, floorNeeded)

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

                                case 2: # (floorNeeded, floorNeeded3, x, x)
                                    match(closestNum(twoCurrentDif, fourCurrentDif)):
                                        case 1: return (floorNeeded, floorNeeded3, floorNeeded2, floorNeeded4)
                                        case 2: return (floorNeeded, floorNeeded3, floorNeeded4, floorNeeded2)

                                case 3: # (floorNeeded, floorNeeded4, x, x)
                                    match(closestNum(twoCurrentDif, threeCurrentDif)):
                                        case 1: return (floorNeeded, floorNeeded4, floorNeeded2, floorNeeded3)
                                        case 2: return (floorNeeded, floorNeeded4, floorNeeded3, floorNeeded2)

                        case 2: # (floorNeeded2, x, x, x)
                            match(closestNum(oneCurrentDif, threeCurrentDif, fourCurrentDif)):
                                case 1: # (floorNeeded2, floorNeeded, x, x)
                                    match(closestNum(threeCurrentDif, fourCurrentDif)):
                                        case 1: return (floorNeeded2, floorNeeded, floorNeeded3, floorNeeded4)
                                        case 2: return (floorNeeded2, floorNeeded, floorNeeded4, floorNeeded3)
                                
                                case 2: # (floorNeeded2, floorNeeded3, x, x)
                                    match(closestNum(oneCurrentDif, fourCurrentDif)):
                                        case 1: return (floorNeeded2, floorNeeded3, floorNeeded, floorNeeded4)
                                        case 2: return (floorNeeded2, floorNeeded3, floorNeeded4, floorNeeded)

                                case 3: # (floorNeeded2, floorNeeded4, x, x)
                                    match(closestNum(oneCurrentDif, threeCurrentDif)):
                                        case 1: return (floorNeeded2, floorNeeded4, floorNeeded, floorNeeded3)
                                        case 2: return (floorNeeded2, floorNeeded4, floorNeeded3, floorNeeded)

                        case 3: # (floorNeeded3, x, x, x)
                            match(closestNum(oneCurrentDif, twoCurrentDif, fourCurrentDif)):
                                case 1: # (floorNeeded3, floorNeeded, x, x)
                                    match(closestNum(twoCurrentDif, fourCurrentDif)):
                                        case 1: return (floorNeeded3, floorNeeded, floorNeeded2, floorNeeded4)
                                        case 2: return (floorNeeded3, floorNeeded, floorNeeded4, floorNeeded3)

                                case 2: # (floorNeeded3, floorNeeded2, x, x)
                                    match(closestNum(oneCurrentDif, fourCurrentDif)):
                                        case 1: return (floorNeeded3, floorNeeded2, floorNeeded, floorNeeded4)
                                        case 2: return (floorNeeded3, floorNeeded2, floorNeeded4, floorNeeded)

                                case 3: # (floorNeeded3, floorNeeded4, x, x)
                                    match(closestNum(oneCurrentDif, twoCurrentDif)):
                                        case 1: return (floorNeeded3, floorNeeded4, floorNeeded, floorNeeded2)
                                        case 2: return (floorNeeded3, floorNeeded4, floorNeeded2, floorNeeded)
                        
                        case 4: # (floorNeeded4, x, x, x)
                            match(closestNum(oneCurrentDif, twoCurrentDif, threeCurrentDif)):
                                case 1: # (floorNeeded4, floorNeeded, x, x)
                                    match(closestNum(twoCurrentDif, threeCurrentDif)):
                                        case 1: return (floorNeeded4, floorNeeded, floorNeeded2, floorNeeded3)
                                        case 2: return (floorNeeded4, floorNeeded, floorNeeded3, floorNeeded2)

                                case 2: # (floorNeeded4, floorNeeded2, x, x)
                                    match(closestNum(oneCurrentDif, threeCurrentDif)):
                                        case 1: return (floorNeeded4, floorNeeded2, floorNeeded, floorNeeded3)
                                        case 2: return (floorNeeded4, floorNeeded2, floorNeeded3, floorNeeded)

                                case 3: # (floorNeeded4, floorNeeded3, x, x)
                                    match(closestNum(oneCurrentDif, twoCurrentDif)):
                                        case 1: return (floorNeeded4, floorNeeded3, floorNeeded, floorNeeded2)
                                        case 2: return (floorNeeded4, floorNeeded3, floorNeeded2, floorNeeded)
                
                elif above1 and above2 and above3 and above4: # If current floor above all other floors
                    match(closestNum(current1Dif, current2Dif, current3Dif, current4Dif)):
                        case 1: # (floorNeeded, x, x, x)
                            match(closestNum(current2Dif, current3Dif, current4Dif)):
                                case 1: # (floorNeeded, floorNeeded2, x, x)
                                    match(closestNum(current3Dif, current4Dif)):
                                        case 1: return (floorNeeded, floorNeeded2, floorNeeded3, floorNeeded4)
                                        case 2: return (floorNeeded, floorNeeded2, floorNeeded4, floorNeeded3)

                                case 2: # (floorNeeded, floorNeeded3, x, x)
                                    match(closestNum(current2Dif, current4Dif)):
                                        case 1: return (floorNeeded, floorNeeded3, floorNeeded2, floorNeeded4)
                                        case 2: return (floorNeeded, floorNeeded3, floorNeeded4, floorNeeded2)

                                case 3: # (floorNeeded, floorNeeded4, x, x)
                                    match(closestNum(current2Dif, current3Dif)):
                                        case 1: return (floorNeeded, floorNeeded4, floorNeeded2, floorNeeded3)
                                        case 2: return (floorNeeded, floorNeeded4, floorNeeded3, floorNeeded2)

                        case 2: # (floorNeeded2, x, x, x)
                            match(closestNum(current1Dif, current3Dif, current4Dif)):
                                case 1: # (floorNeeded2, floorNeeded, x, x)
                                    match(closestNum(current3Dif, current4Dif)):
                                        case 1: return (floorNeeded2, floorNeeded, floorNeeded3, floorNeeded4)
                                        case 2: return (floorNeeded2, floorNeeded, floorNeeded4, floorNeeded3)
                                
                                case 2: # (floorNeeded2, floorNeeded3, x, x)
                                    match(closestNum(current1Dif, current4Dif)):
                                        case 1: return (floorNeeded2, floorNeeded3, floorNeeded, floorNeeded4)
                                        case 2: return (floorNeeded2, floorNeeded3, floorNeeded4, floorNeeded)

                                case 3: # (floorNeeded2, floorNeeded4, x, x)
                                    match(closestNum(current1Dif, current3Dif)):
                                        case 1: return (floorNeeded2, floorNeeded4, floorNeeded, floorNeeded3)
                                        case 2: return (floorNeeded2, floorNeeded4, floorNeeded3, floorNeeded)

                        case 3: # (floorNeeded3, x, x, x)
                            match(closestNum(current1Dif, current2Dif, current4Dif)):
                                case 1: # (floorNeeded3, floorNeeded, x, x)
                                    match(closestNum(current2Dif, current4Dif)):
                                        case 1: return (floorNeeded3, floorNeeded, floorNeeded2, floorNeeded4)
                                        case 2: return (floorNeeded3, floorNeeded, floorNeeded4, floorNeeded3)

                                case 2: # (floorNeeded3, floorNeeded2, x, x)
                                    match(closestNum(current1Dif, current4Dif)):
                                        case 1: return (floorNeeded3, floorNeeded2, floorNeeded, floorNeeded4)
                                        case 2: return (floorNeeded3, floorNeeded2, floorNeeded4, floorNeeded)

                                case 3: # (floorNeeded3, floorNeeded4, x, x)
                                    match(closestNum(current1Dif, current2Dif)):
                                        case 1: return (floorNeeded3, floorNeeded4, floorNeeded, floorNeeded2)
                                        case 2: return (floorNeeded3, floorNeeded4, floorNeeded2, floorNeeded)
                        
                        case 4: # (floorNeeded4, x, x, x)
                            match(closestNum(current1Dif, current2Dif, current3Dif)):
                                case 1: # (floorNeeded4, floorNeeded, x, x)
                                    match(closestNum(current2Dif, current3Dif)):
                                        case 1: return (floorNeeded4, floorNeeded, floorNeeded2, floorNeeded3)
                                        case 2: return (floorNeeded4, floorNeeded, floorNeeded3, floorNeeded2)

                                case 2: # (floorNeeded4, floorNeeded2, x, x)
                                    match(closestNum(current1Dif, current3Dif)):
                                        case 1: return (floorNeeded4, floorNeeded2, floorNeeded, floorNeeded3)
                                        case 2: return (floorNeeded4, floorNeeded2, floorNeeded3, floorNeeded)

                                case 3: # (floorNeeded4, floorNeeded3, x, x)
                                    match(closestNum(current1Dif, current2Dif)):
                                        case 1: return (floorNeeded4, floorNeeded3, floorNeeded, floorNeeded2)
                                        case 2: return (floorNeeded4, floorNeeded3, floorNeeded2, floorNeeded)
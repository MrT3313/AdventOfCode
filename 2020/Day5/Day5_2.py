from Day5_1 import binaryBoarding_maxSeatID

def binaryBoarding_findSeatID():
    maxID, passports = binaryBoarding_maxSeatID()

    seatIDs = [passport[3] for passport in passports]
    seatIDs.sort()

    for idx, num in enumerate(seatIDs):
        if idx == len(seatIDs) - 2: 
            return False

        if seatIDs[idx + 1] - seatIDs[idx] != 1: 
            result = seatIDs[idx] + 1

            if result != seatIDs[idx + 1] - 1:
                print('Fails Gap Constraint')

            return result

# TEST
# result = binaryBoarding_findSeatID()
# print(result)
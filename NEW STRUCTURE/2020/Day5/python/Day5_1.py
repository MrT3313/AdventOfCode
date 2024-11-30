import math

def readInputData():
    # Get Input Data
    f = open("2020/Day5/Day5_input.txt", "r")
    input = f.read()
    dataArray = input.split("\n\n")[0]
    f.close()

    return dataArray

def getData(data, fullString):

    def recurse(modifiedData, str):
        # Base Case
        if len(modifiedData) == 1:
            return modifiedData[0]

        if str[0] == "F" or str[0] == "L":
            midIdx = len(modifiedData) // 2
            half = modifiedData[:midIdx]
        if str[0] == "B" or str[0] == "R":
            midIdx = len(modifiedData) // 2
            half = modifiedData[midIdx:]
            
        return recurse(half, str[1:])
    
    result = recurse(data, fullString)
    
    return result

def getMaxSeatID(passports):
    maxID = -math.inf

    for _ in passports:
        if _[3] > maxID:
            maxID = _[3]

    return maxID

def binaryBoarding_calculateSeatIDs():
    # Get Data
    data = readInputData()
    dataArray = data.split("\n")
    num_of_rows = 128
    num_of_cols = 8

    # Modify Data
    modifiedArray = [[
        string,     # full string
        string[:7], # rowData
        string[7:], # colData
    ] for string in dataArray]

    # Loop through boarding passes
    for boardingPass in modifiedArray:
        # Get row and column data
        row = getData(list(range(0, num_of_rows)),  boardingPass[1])
        col = getData(list(range(0, num_of_cols)),    boardingPass[2])

        # Calculate seatID
        seatID = row * 8 + col
        boardingPass.append(seatID)

    result = getMaxSeatID(modifiedArray)
    return result, modifiedArray

# TEST 
# result = binaryBoarding_calculateSeatIDs()
# print(result[0])
# # print(result[1])
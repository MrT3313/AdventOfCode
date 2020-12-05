import re
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

def binaryBoarding():
    # Get Data
    data = readInputData()
    dataArray = data.split("\n")
    num_of_rows = 128
    num_of_cols = 8
    result = -math.inf

    # Modify Data
    modifiedArray = [[
        string,
        string[:7], # rowData
        string[7:], # colData
    ] for string in dataArray]

    # Loop through boarding passes
    for boardingPass in modifiedArray:
        # [0] = full string
        # [1] = row data
        # [2] = col data

        # Get row and column data
        row = getData(list(range(0, num_of_rows)),  boardingPass[1])
        col = getData(list(range(0, num_of_cols)),    boardingPass[2])

        # Calculate seatID
        seatID = row * 8 + col

        # Update max seatID
        if seatID > result:
            result = seatID

    return result

# TEST 
# result = binaryBoarding()
# print(result)
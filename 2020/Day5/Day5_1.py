import re

def readInputData():
    # Get Input Data
    f = open("2020/Day5/Day5_input.txt", "r")
    input = f.read()
    dataArray = input.split("\n\n")[0]
    f.close()

    return dataArray


def binaryBoarding():

    data = readInputData()
    dataArray = data.split("\n")
    num_of_rows = 127

    modifiedArray = [[
        string,
        string[:7], # rowData
        string[7:], # colData
    ] for string in dataArray]

    for boardingPass in modifiedArray:
        # [0] = full string
        # [1] = row data
        # [2] = col data
        
        def getRow(data, fullString):
            print(fullString)

            def recurse(modifiedData, str):
                # Base Case
                if len(modifiedData) == 1:
                    print('GET number')
                    return modifiedData[0]

                print(modifiedData)
                print(str)
                if str[0] == "F":
                    midIdx = len(modifiedData) // 2
                    print('MID IDX ', midIdx)
                    half = modifiedData[:midIdx]
                    print('HALF -- F', half)
                    # pass
                if str[0] == "B":
                    midIdx = len(modifiedData) // 2
                    print('MID IDX ', midIdx)
                    half = modifiedData[midIdx:]
                    print('HALF -- B', half)
                    
                    # exit()
                return recurse(half, str[1:])
            
            result = recurse(data, fullString)
            return result

        # row = getRow(list(range(0, 128)), boardingPass[1])
        row = getRow(list(range(0, 128)), 'FBFBBFF')
        print(row)
        exit()

    return 'BLARG'

# TEST 
result = binaryBoarding()
print(result)
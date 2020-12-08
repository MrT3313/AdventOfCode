import pandas as pd

def readInputData():
    # Get Input Data
    f = open("2020/Day8/input.txt", "r")
    # f = open("2020/Day8/testInput_pt1.txt", "r")
    input = f.read()
    dataArray = input.split("\n")
    f.close()

    return [readLine(x) for x in dataArray]

def readLine(line):
    split = line.split(' ')

    # _variables_
    action = split[0]
    amount = split[1]

    direction = None
    if amount[0] == "+":
        direction = '+'  
    if amount[0] == "-":
        direction = '-'  
    amount = int(amount[1:])

    return [action, direction, amount]

def solve():
    data = readInputData()
    # print(data)

    resultAcc = 0
    idx = 0
    cache = []
    run = True

    while run == True: 
        # Check idx
        if idx in cache:
            run = False
            break
        else: 
            cache.append(idx)

        currData = data[idx]
        print(idx, currData)

        if currData[0] == 'nop':
            idx += 1
            continue

        if currData[0] == 'acc':
            if currData[1] == '+':
                resultAcc += currData[2]
            if currData[1] == '-':
                resultAcc -= currData[2]
            idx += 1
            continue

        if currData[0] == 'jmp':
            if currData[1] == '+':
                idx += currData[2]
            if currData[1] == '-':
                idx -= currData[2]
            continue

    return resultAcc, cache

# RESULT
result, seen = solve()
print('RESULT',result)
print('SEEN',seen)
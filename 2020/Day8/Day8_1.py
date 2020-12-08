def readInputData():
    # Get Input Data
    f = open("2020/Day8/input.txt", "r")
    # f = open("2020/Day8/testInput.txt", "r")
    input = f.read()
    dataArray = input.split("\n")
    f.close()

    return dataArray

def prepData(data):
    return [readLine(x) for x in data]

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
    amount = amount[1:]

    return action, direction, amount

def solve():
    data = readInputData()
    cleanData = prepData(data)

    seen = []
    counter = 0
    idx = 0

    print(cleanData)
    while idx < len(cleanData):
        print('COUNTER: ', counter, 'IDX: ', idx)
        
        # Check for repeat command
        if idx in seen: 
            break
        else:
            seen.append(idx)
        
        # Get current data
        currData = cleanData[idx]

        # Perform action
        if currData[0] == 'nop':
            print('nop')
            idx += 1

        if currData[0] == 'acc':
            print('acc')
            if currData[1] == '+':
                counter += int(currData[2])
            if currData[1] == '-':
                counter -= int(currData[2])
            idx += 1

        if currData[0] == 'jmp':
            print('jmp')
            if currData[1] == '+':
                idx += int(currData[2])
            if currData[1] == '-':
                idx -= int(currData[2])
    
    return counter, seen

# RESULT
# result, seen = solve()
# print('RESULT',result)
# print('SEEN',seen)
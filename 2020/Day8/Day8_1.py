def readInputData():
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

def solve(data, part2=False, DEBUG=False):
    '''
    
        data = [
            [ 'npm' | 'acc' | jmp ,       '+' | '-',      int ], 
            ...
        ]
    '''
    resultAcc = 0
    idx = 0
    cache = []
    run = True

    while run == True: 
        if DEBUG: 
            print('IDX: ', idx, 'RESULT: ', resultAcc)

        # Exit Conditions
        ## Check idx
        if idx in cache:
            run = False
            break
        else: 
            cache.append(idx)
        
        ## Check Part 2 Modification => last line check
        if part2 == True and idx == len(data):
            run = False
            break 
        
        # Do Action
        currData = data[idx]
        ## No Action
        if currData[0] == 'nop':
            idx += 1
            continue

        ## Increment Counter
        if currData[0] == 'acc':
            if currData[1] == '+':
                resultAcc += currData[2]
            if currData[1] == '-':
                resultAcc -= currData[2]
            idx += 1
            continue

        ## Jump
        if currData[0] == 'jmp':
            if currData[2] == 0:
                run = False
                break
            
            if currData[1] == '+':
                idx += currData[2]
            if currData[1] == '-':
                idx -= currData[2]
            continue

    return resultAcc, cache

# RESULT
# result, cache = solve(readInputData())
# print('RESULT',result)
# print('cache',cache)
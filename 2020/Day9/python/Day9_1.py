def readInputData():
    f = open("2020/Day9/Day9_input.txt", "r")
    # f = open("2020/Day9/Day9_testData_pt1.txt", "r")
    input = f.read()
    dataArray = input.split("\n")
    f.close()

    return [int(_) for _ in dataArray]

def recurse(data, currentIdx, cache):
    # Base Case
    if currentIdx == len(data) - 1:
        return False

    # _variables_
    available = set([_ for _ in cache])
    num = data[currentIdx]

    for cacheNum in cache:
        found = False
        available.remove(cacheNum)
        newTarget = num - cacheNum

        if newTarget in available:
            found = True
            break
        else:
            available.add(cacheNum)
    
    # Conditional Return
    if found == True:
        currentIdx += 1
        cache.pop(0)
        cache.append(data[currentIdx - 1])

        return recurse(data, currentIdx, cache)

    if found == False:
        return num

def solve():
    data = readInputData()
    # print(data)

    '''
        preamble => 25 characters

        preamble + 1 = sum of ANY combination of prev 25
    '''

    # _variables_
    preamble = 25
    # preamble = 5      # Test Data

    window = [ 0, preamble-1 ]
    currentIdx = preamble

    # Create Pool
    cache = data[window[0]:window[1] + 1]
    print('CACHE', cache)

    return recurse(data, currentIdx, cache)

# TEST
# result = solve()
# print(result)
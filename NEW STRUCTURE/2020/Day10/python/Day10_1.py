def readInputData():
    f = open("2020/Day10/Day10_input.txt", "r")
    # f = open("2020/Day10/Day10_testData1_pt1.txt", "r")
    input = f.read()
    dataArray = input.split("\n")
    f.close()

    return [int(_) for _ in dataArray]

def recurse(data, idx, result, prev):
    # EDGE CASE: 
    if idx >= len(data):
        return result

    # GET: current num 
    num = data[idx]

    # UPDATE: result
    result[1].append(num)
    result[2].append(num - prev)

    # RECURSE: 
    return recurse(data, idx + 1, result, num)

def getUniqueCount(data):
    cache = {}
    for _ in data[2]:
        if _ not in cache:
            cache[_] = 1
        else:
            cache[_] += 1
    return cache


def solve():
    # GET: input data
    data = readInputData()
    data.sort()

    # VARIABLES:
    outletJolts = 0
    result = [outletJolts, [],[]]

    # TRAVERSE DATA
    traversedData = recurse(data, 0, result, outletJolts)

    # CALCULATE: cound unique jumps
    uniqueCount = getUniqueCount(traversedData)

    # UPDATE:
    # Final 3+ difference from adapter to phone
    uniqueCount[3] += 1

    # RETURN:
    return uniqueCount[1] * uniqueCount[3]

# TEST
# result = solve()
# print(result)

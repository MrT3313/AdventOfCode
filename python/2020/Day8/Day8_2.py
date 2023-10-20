from Day8_1 import readLine, solve

def readInputData():
    # Get Input Data
    f = open("2020/Day8/input.txt", "r")
    # f = open("2020/Day8/testInput_pt2.txt", "r")
    input = f.read()
    dataArray = input.split("\n")
    f.close()

    return [readLine(x) for x in dataArray]

def swap(data):
    if data[0] == 'nop':
        data[0] = 'jmp'
        return data

    if data[0] == 'jmp':
        data[0] = 'nop'
        return data

def solve_part2(data):
    idx = 0
    cache = []
    for _ in data:
        # Check for no change
        if data[idx][0] == 'acc':
            idx += 1
            continue
        
        # Swap
        data[idx] = swap(data[idx])

        # Solve this version of the input data
        result, cache = solve(data, part2=True)
        
        # Did it hit the part2 base condition?
        if cache[-1] == len(data):
            return result, cache
        else:
            # Swap back
            data[idx] = swap(data[idx])
            # Increment
            idx += 1

# TEST
# data = readInputData()
# result = solve_part2(data)
# print(result)

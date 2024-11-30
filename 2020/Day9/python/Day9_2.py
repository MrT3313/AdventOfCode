from Day9_1 import solve as getProblemNumber
from Day9_1 import readInputData

def recurse(data, target, startPointer, window):
    # _variables_
    found = False
    endPointer = startPointer + window - 1
    sum = data[startPointer]
    
    # Main loop
    while endPointer < len(data):
        # Get Current Range
        range = data[startPointer:endPointer + 1]

        # Increment Sum
        sum += range[-1]

        # Check against target
        if sum == target:
            found = True
            break
        # Edge Case => save processing
        elif sum > target:
            break

        # Increment End Pointer
        endPointer += 1
    
    # Conditional Return
    if found == True:
        return range
    if found == False:
        startPointer += 1
        return recurse(data, target, startPointer, window)


def solve():
    data = readInputData()
    num = getProblemNumber()
    
    startPointer = 0
    window = 2

    range = recurse(data, num, startPointer, window)

    range.sort()
    min = range[0]
    max = range[-1]

    return min + max


# Test
result = solve()
print(result)


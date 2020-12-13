def readInputData():
    f = open("2020/Day13/Day13_input.txt", "r")
    # f = open("2020/Day13/Day13_testData_pt1.txt", "r")
    input = f.read()
    data = input.split("\n")
    f.close()

    return int(data[0]), [int(_) for _ in data[1].split(',') if _ != 'x']

def recurse(time, bussArr):
    # LOOP: through all available buss's
    for _ in bussArr:
        if time % _ == 0: 
            return time, _
    
    # RECURSE: increment time
    return recurse(time + 1, bussArr)

def solve(earliestDeparturetime, time, buss): 
    return (time - earliestDeparturetime) * buss

def part1():
    # GET: input data
    earliestDeparture, bussIDs  = readInputData()

    # FIND: first available buss & time
    time, buss = recurse(earliestDeparture, bussIDs)
    
    # SOLVE: based on custom problem condition
    return solve(earliestDeparture, time, buss)

# TEST
# result = part1()
# print(result)
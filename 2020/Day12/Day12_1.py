def readInputData():
    f = open("2020/Day12/Day12_input.txt", "r")
    # f = open("2020/Day12/Day12_testData_pt1.txt", "r")
    input = f.read()
    dataArray = input.split("\n")
    f.close()

    return [_ for _ in dataArray]


def moveShip(position, direction, action, amount):
    # UPDATE: forward
    # NOTES: simply use the "F" as an indicator to update the action the ships current direction and let the regular updating flow
    if action == "F":
        action = direction

    # UPDATE: horizontal
    if action == "W":
        position[0] -= amount
    if action == "E":
        position[0] += amount
    
    # UPDATE: vertical
    if action == "S":
        position[1] -= amount
    if action == "N":
        position[1] += amount

    # RETURN: new position
    return position

def turnShip(direction, action, amount):
    # _variables_
    directions = ["N", "E", "S", "W"]
    
    # CALCULATE: rotation
    rotation = amount //  90

    # GET: current direction index
    idx = directions.index(direction)

    # UPDATE: direction
    if action == "L":
        newDirection = directions[(idx - rotation) % len(directions)]
    if action == "R":
        newDirection = directions[(idx + rotation) % len(directions)]
        
    # RETURN: new direction
    return newDirection

def recurse(data, position, direction, movementArr, turningArr):
    # BASE CASE:
    if len(data) == 0: 
        return position
    
    # GET: instruction
    currInstruction = data[0]
    print('')
    print('-New Loop Start-')
    print('CURRENT INSTRUCTION: ', currInstruction)
    print('CURRENT POSITION: ', position)
    print('CURRENT DIRECTION: ', direction)

    # GET: instruction arguments
    action = currInstruction[0]
    num = int(currInstruction[1:])

    # CONDITIONAL: choose correction action
    ## MOVE: ship
    if action in movementArr:
        newPosition = moveShip(position, direction, action, num)
        
        return recurse(data[1:], newPosition, direction, movementArr, turningArr)
    ## TURN: ship
    elif action in turningArr:
        newDirection = turnShip(direction, action, num)

        return recurse(data[1:], position, newDirection, movementArr, turningArr)

def solve():
    # GET: input data
    data = readInputData()

    # _variables_
    STARTING_POSITION = [0,0]                       # [x,y]
    STARTING_DIRECTION = "E"
    MOVEMENT = ["F", "N", "S", "E", "W"]
    TURNING = ["L", "R"]

    # RECURSE
    finalPosition = recurse(data, STARTING_POSITION, STARTING_DIRECTION, MOVEMENT, TURNING)

    # RETURN
    return abs(finalPosition[0]) + abs(finalPosition[1])

# TEST
# result = solve()
# print(result)
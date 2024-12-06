import pprint

def readInputFile(test_input=False):
    if test_input:
        f = open("../test_input.txt", "r")
    else:
        f = open("../input.txt", "r")

    data = f.read()
    lines = data.splitlines()
    f.close()

    return lines

movement = {
    "^": (0, -1), # up
    ">": (1, 0), # right
    "v": (0, 1), # down
    "<": (-1, 0) # left
}

def countVisitedCells(matrix):
    count = 0
    visited_chars = {'X', '^', '>', 'v', '<'}

    # Loop through each cell in the matrix
    for row in matrix:
        for cell in row:
            if cell in visited_chars:
                count += 1

    return count

def findGuardStartingPoint(matrix):
    # Define the characters we're looking for
    guard_chars = {'^', '>', '<', 'v'}
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] in guard_chars:
                return (i, j, matrix[i][j])
    
    return None

def guardFoundFall(direction):
    # TURN: right
    if (direction == "^"): return ">"
    if (direction == ">"): return "v"
    if (direction == "v"): return "<"
    if (direction == "<"): return "^"
    

def getGuardMovementVector(curr_row, curr_col, direction_char, matrix):
    # VARIABLES
    movement_vector = []
    matrix_height = len(matrix)
    matrix_width = len(matrix[0])
    delta_col, delta_row = movement[direction_char]

    # START: from current position
    row, col = curr_row, curr_col

    # LOOP: through fixed direction until hitting:
    #       - a wall ("#") OR
    #       - matrix boundary
    while True:
        # CALCULATE: next position
        row += delta_row
        col += delta_col
        
        # CHECK: for out of bounds
        if (row < 0 or row >= matrix_height or 
            col < 0 or col >= matrix_width):
            return [False, row - delta_row, col - delta_col]  
        # CHECK: for hit wall ("#")
        elif matrix[row][col] == '#':
            direction_char  = guardFoundFall(direction_char)
            row = row - delta_row
            col = col - delta_col
            break
        else:
            matrix[row - delta_row][col - delta_col] = "X"
            matrix[row][col] = direction_char
        
            # ADD: current position to movement vector
            movement_vector.append((row, col))

        # pprint.pprint(matrix)
        # print(f'--')
    
    return [direction_char, row, col]

def part1(data):

    # VARIABLES
    matrix_height = len(data)
    matrix_width = len(data[0])
    current_guard_direction = None

    # CREATE: matrix
    matrix = [
        [
            data[row][col]
            for col in range(matrix_width)
        ] 
        for row in range(matrix_height)
    ]
    # pprint.pprint(matrix, width=800, compact=False)

    # FIND: guard starting point
    (row, col, val) = findGuardStartingPoint(matrix)

    # GET: guard movement vector
    [new_direction, guard_row, guard_col] = getGuardMovementVector(row, col, val, matrix)
    while new_direction != False:
        [new_direction, guard_row, guard_col] = getGuardMovementVector(
            guard_row, guard_col, new_direction, matrix
        )

    return countVisitedCells(matrix)



# -- #
data = readInputFile()
# data = readInputFile(test_input=True)
result = part1(data)
print(f'THE RESULT : {result}')
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
    "^": (0, -1), 
    ">": (1, 0),  
    "v": (0, 1),  
    "<": (-1, 0)  
}

def findGuardStartingPoint(matrix):
    guard_chars = {'^', '>', '<', 'v'}
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] in guard_chars:
                return (i, j, matrix[i][j])
    
    return None

def guardFoundWall(direction):
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
            direction_char = guardFoundWall(direction_char)
            row = row - delta_row
            col = col - delta_col
            break
        else:
            # matrix[row - delta_row][col - delta_col] = "X"
            matrix[row][col] = direction_char
        
            # ADD: current position to movement vector
            movement_vector.append((row, col))
    
    return [direction_char, row, col]

def isInfiniteLoop(matrix, start_row, start_col, start_direction):
    # VARIABLES
    visited_states = set()
    curr_row, curr_col = start_row, start_col
    curr_direction = start_direction
    
    while True:
        # CONGIRE: state tuple (row, col, direction)
        state = (curr_row, curr_col, curr_direction)
        
        # CHECK: have we been in this state before?
        if state in visited_states:
            return True
        
        visited_states.add(state)
        
        # GET: next position
        [new_direction, new_row, new_col] = getGuardMovementVector(
            curr_row, curr_col, curr_direction, matrix
        )
        
        # IF: out of bounds, not an infinite loop
        if new_direction == False:
            return False
            
        curr_row, curr_col = new_row, new_col
        curr_direction = new_direction

def countPossibleWallsLeadingToInfiniteLoop(data):
    matrix_height = len(data)
    matrix_width = len(data[0])
    wall_count = 0
    
    # FIND: guard starting point
    (start_row, start_col, start_direction) = findGuardStartingPoint(data)
    
    # LOOP: any add wall at each empty cell
    for row in range(matrix_height):
        for col in range(matrix_width):
            if data[row][col] == '.':
                # Create new matrix with added wall
                test_matrix = [row[:] for row in data]
                test_matrix[row][col] = '#'
                
                # Test if this creates an infinite loop
                if isInfiniteLoop(test_matrix, start_row, start_col, start_direction):
                    wall_count += 1
    
    return wall_count

def part2(data):
    # CREATE: matrix
    matrix = [list(row) for row in data]
    return countPossibleWallsLeadingToInfiniteLoop(matrix)

# -- #
data = readInputFile()
# data = readInputFile(test_input=True)
result = part2(data)
print(f'THE RESULT : {result}')
import pprint
from typing import List, Tuple
import copy

def readInputFile(test_input=False):
    if test_input:
        f = open("../test_input.txt", "r")
    else:
        f = open("../input.txt", "r")

    data = f.read()
    lines = data.splitlines()
    f.close()

    return lines

directions = [
    (-1, 0),   
    (0, 1),    
    (1, 0),    
    (0, -1)    
]

wall_collision_directions = {
    'from_top': '<',     
    'from_right': '^',  
    'from_bottom': '>',   
    'from_left': 'v',   
}

def part2(data):
    # VARIABLES
    matrix_height = len(data)
    matrix_width = len(data[0])

    # CREATE: matrix
    matrix = [
        [
            data[row][col]
            for col in range(matrix_width)
        ] 
        for row in range(matrix_height)
    ]
    # pprint.pprint(matrix)

    # CONFIGURE: known walls
    walls = set() # key = tuple -> (row, col)
    for row in range(matrix_height):
        for col in range(matrix_width):
            if matrix[row][col] == "#":
                walls.add((row, col))
    print(f'THE WALLS : {walls}')

    # VARIABLES: Matrix Loop
    count = 0
    current_position = None
    previous_position = None
    next_position = None

    # LOOP: through each cell in matrix
    for ri, row in enumerate(matrix):
        for ci, col in enumerate(row):
            print(f'🔄🔄🔄🔄')
            count += 1
            current_position = (ri, ci)
            print(f'current position : {current_position} > {matrix[ri][ci]}')

            # matrix[current_position[0]][current_position[1]] = "🧙"
            # matrix[current_position[0]][current_position[1]] = "🧙"
            # pprint.pprint(matrix)

            # FILTER: for relevant walls to current position
            relevant_walls = set()
            for wall in walls:
                # Check if wall is in same row
                if wall[0] == current_position[0]:
                    relevant_walls.add(wall)
                # Check if wall is in same column
                elif wall[1] == current_position[1]:
                    relevant_walls.add(wall)
            print(f'Relevant walls for position {current_position}:\n\t {relevant_walls}')

            # print(f'DEBUG - !')
            # pprint.pprint(matrix)
                
            # CHECK: for > 0 relevant walls
            # if len(relevant_walls) == 0:
            #     print(f'NO RELEVANT WALLS -> SKIPPING THIS ITERATION')
            #     # break
            #     continue

            matrix_copy = matrix

            # Initialize neighbors list
            neighbors = []
            # Check boundaries and add valid neighbors
            if ri >= 1:
                neighbors.append((ri - 1, ci))
            if ri < len(matrix) - 1:  # Changed: Added -1 to prevent out of bounds
                neighbors.append((ri + 1, ci))
            if ci >= 1:
                neighbors.append((ri, ci - 1))
            if ci < len(matrix[0]) - 1:  # Changed: Added -1 to prevent out of bounds
                neighbors.append((ri, ci + 1))
            print(f'({ri}, {ci}) NEIGHBORS : {neighbors}')

            neighbor_results = []
            incoming_direction = None


            for neighbor_row, neighbor_col in neighbors:
                print(f'CURRENT NEIGHBOR : ({neighbor_row}, {neighbor_col})')
                # Determine incoming direction based on neighbor position
                if neighbor_row == ri and neighbor_col > ci:
                    incoming_direction = 'from_left'
                if neighbor_row == ri and neighbor_col < ci:
                    incoming_direction = 'from_right'
                if neighbor_col == ci and neighbor_row > ri:
                    incoming_direction = 'from_bottom'
                if neighbor_col == ci and neighbor_row < ri:
                    incoming_direction = 'from_top'
                
                print(f'SIMULARED INCOMING DIRECTION : {incoming_direction}')

                #
                new_direction = wall_collision_directions[incoming_direction]
                print(f'SIMULARED NEW DIRECTION : {new_direction}')
                starting_neighbor_value = matrix[neighbor_row][neighbor_col]
                matrix[neighbor_row][neighbor_col] = new_direction

                starting_value = matrix[current_position[0]][current_position[1]]
                matrix[current_position[0]][current_position[1]] = '🧱'

                print(f'----- INITIAL NEIGHBOR RECURSION CALL -----')
                fresh_matrix = copy.deepcopy(matrix)
                neighbor_results.append(
                    recurse_2(
                        matrix=fresh_matrix,
                        new_wall_position=current_position,
                        new_direction=new_direction,
                        current_position=(neighbor_row,neighbor_col)
                    )
                )

                matrix[current_position[0]][current_position[1]] = starting_value
                matrix[neighbor_row][neighbor_col] = starting_neighbor_value

                print(f'🎉 NEIGHBOR RESULTS : {neighbor_results}')
                
            print(f'FUCK')
            # pprint.pprint(result)
            

movement_directions = {
    "^": (-1,0),
    ">": (0,1),
    "v": (1,0),
    "<": (0,-1),
}
def recurse_2(
    matrix, # HOW TO MAKE SURE THIS IS A CLEAN MATRIX AND UNEFFECTED BY ANY OTEHR RECURSIVE CALLS & MANIUPLATIONS ON THE MATRIX?
    new_wall_position,
    new_direction,
    current_position,
):
    print(f'===== RECURSION ===== :\n\tWall Proposal > {(new_wall_position[0], new_wall_position[1])}\n\tCurrent Position > {(current_position[0], current_position[1])}')
    print(f'NEW DIRECTION: {new_direction}')

    next_row = current_position[0] + movement_directions[new_direction][0]
    next_col = current_position[1] + movement_directions[new_direction][1]
    print(f'NEXT CELL : ({next_row}, {next_col})')

    if (
        next_row < 0 or 
        next_col < 0 or 
        next_row >= len(matrix) or 
        next_col >= len(matrix[0])
    ):
        print(f'OUT OF BOUNDS')
        pprint.pprint(matrix)
        return False
    else:

        next_val = matrix[next_row][next_col]
        print(f'NEXT VALUE : {next_val}')

        if next_val == "#":
            print(f'WHAT DO DO HERE!!!!!!!!! :\n\tCurrent Position : ({current_position[0]}, {current_position[1]})\n\tNext Position : ({next_row}, {next_col})')

            # CALCULATE NEW DIRECTION
            if (
                next_row == current_position[0] and 
                next_col > current_position[1]
            ):
                incoming_direction = 'from_left'

            if (
                next_row == current_position[0] and
                next_col < current_position[1]
            ):
                incoming_direction = 'from_right'

            if (
                next_col == current_position[1] and
                next_row > current_position[0]
            ):
                incoming_direction = 'from_top'

            if (
                next_col == current_position[1] and
                next_row < current_position[0]
            ):
                incoming_direction = 'from_bottom'

            print(f'INCOMING COLISION DIRECTION : {incoming_direction}')
            new_direction = wall_collision_directions[incoming_direction]
            print(f'NEW COLISION DIRECTION : {new_direction}')

            pprint.pprint(matrix)
            matrix[current_position[0]][current_position[1]] = new_direction
            
            next_next_row = current_position[0] + movement_directions[new_direction][0]
            next_next_col = current_position[1] + movement_directions[new_direction][1]

            if (
                next_next_row < 0 or 
                next_next_col < 0 or 
                next_next_row >= len(matrix) or 
                next_next_col >= len(matrix[0])
            ):
                print(f'OUT OF BOUNDS')
                pprint.pprint(matrix)
                return False

            movement_char = None
            if new_direction == "^" or new_direction == "v":
                movement_char = "|"
            if new_direction == "<" or new_direction == ">":
                movement_char = "-"
            matrix[next_next_row][next_next_col] = movement_char



            recurse_2(
                matrix=matrix,
                new_wall_position=new_wall_position,
                new_direction=new_direction,
                current_position=(next_next_row, next_next_col)
            )

            # print(f'Check - 1')
            # pprint.pprint(matrix)

        else:
            movement_char = None
            if new_direction == "^" or new_direction == "v":
                movement_char = "|"
            if new_direction == "<" or new_direction == ">":
                movement_char = "-"
            
            matrix[next_row][next_col] = movement_char
            return recurse_2(
                matrix,new_wall_position,new_direction, (next_row, next_col)
            )
    
    # print(f'Check - Final')
    # pprint.pprint(matrix)

    pass

# -- #
# data = readInputFile()
data = readInputFile(test_input=True)
result = part2(data)
print(f'THE RESULT : {result}')
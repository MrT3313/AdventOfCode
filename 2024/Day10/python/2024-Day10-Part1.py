import pprint
from typing import List, Set, Tuple, Dict

def readInputFile(test_input=False):
    if test_input:
        f = open("../test_input.txt", "r")
    else:
        f = open("../input.txt", "r")

    data = f.read()
    lines = data.splitlines()
    f.close()

    return lines

def getNeighbors(position: Tuple[int, int], matrix: List[List[int]]) -> List[Tuple[int, int]]:
    """
    Returns valid neighbors that are exactly one height greater than current position.
    """
    row, col = position
    current_value = matrix[row][col]
    
    # If we're at 9, no valid neighbors
    if current_value == 9:
        return []
    
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    
    for d_row, d_col in directions:
        new_row, new_col = row + d_row, col + d_col
        
        if (0 <= new_row < len(matrix) and 
            0 <= new_col < len(matrix[0]) and 
            matrix[new_row][new_col] == current_value + 1):  # Key change: only allow exactly one height greater
            neighbors.append((new_row, new_col))
    
    return neighbors
    
def part1(data):
    # VARIABLES
    matrix_height = len(data)
    matrix_width = len(data[0])
    trail_heads = []
    all_successful_paths = []

    # CREATE: matrix
    matrix = [
        [
            int(data[row][col])
            for col in range(matrix_width)
        ] 
        for row in range(matrix_height)
    ]
    # pprint.pprint(matrix, width=400, compact=False)
    pprint.pprint(matrix)

    # FIND: all trail heads
    for row in range(matrix_height):
        for col in range(matrix_width):
            if matrix[row][col] == 0:
                trail_heads.append((row, col))
    print(f'Trail Heads : {trail_heads}')

    # LOOP: through all trail heads - initiate DFS recursion
    total_paths = 0
    for th in trail_heads:
        print(f'> Current Trailhead : {th}')
        paths, successful_paths = depthFirstSearch(matrix, th)  # Modified to receive both count and paths
        total_paths += paths
        all_successful_paths.extend(successful_paths)  # Store the successful paths
        print(f'> Paths found: {paths}')
        print(f'> Successful paths: {successful_paths}')
        print(f'\n')
    
    return total_paths, all_successful_paths

def depthFirstSearch(
    matrix, 
    position, 
    visited=None, 
    current_path=None
):
    if visited is None:
        visited = set()
    if current_path is None:
        current_path = []
    
    row, col = position
    current_value = matrix[row][col]
    
    # If we've visited this position before, this isn't a new path
    if position in visited:
        return 0, []
    
    # Add current position to path and visited set
    current_path.append(position)
    visited.add(position)
    
    # If we hit a 9, we've found a valid path
    if current_value == 9:
        result_path = current_path[:]
        current_path.pop()
        visited.remove(position)
        return 1, [result_path]
    
    # Get valid neighbors (only those exactly one height greater)
    neighbors = getNeighbors(position, matrix)
    
    # Recurse
    paths_found = 0
    successful_paths = []
    for next_pos in neighbors:
        new_paths, new_successful_paths = depthFirstSearch(
            matrix, 
            next_pos, 
            visited.copy(),  # Important: pass a copy of visited
            current_path
        )
        paths_found += new_paths
        successful_paths.extend(new_successful_paths)
    
    # Backtrack
    current_path.pop()
    visited.remove(position)
    
    return paths_found, successful_paths

# -- #

# data = readInputFile()
data = readInputFile(test_input=True)
result = part1(data)
print(f'THE RESULT : {result}')
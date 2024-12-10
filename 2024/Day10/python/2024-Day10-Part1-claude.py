from collections import defaultdict
import pprint
from typing import List, Set, Tuple, Dict

def read_input_file(test_input=False):
    filename = "../test_input.txt" if test_input else "../input.txt"
    with open(filename, "r") as f:
        return f.read().splitlines()

def create_matrix(data: List[str]) -> List[List[int]]:
    return [[int(char) for char in line] for line in data]

def get_valid_neighbors(matrix: List[List[int]], position: Tuple[int, int]) -> List[Tuple[int, int]]:
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
            matrix[new_row][new_col] == current_value + 1):
            neighbors.append((new_row, new_col))
    
    return neighbors

def find_trailheads(matrix: List[List[int]]) -> List[Tuple[int, int]]:
    """Find all positions with height 0."""
    trailheads = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                trailheads.append((row, col))
    return trailheads

def find_endpoints(matrix: List[List[int]]) -> Set[Tuple[int, int]]:
    """Find all positions with height 9."""
    endpoints = set()
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 9:
                endpoints.add((row, col))
    return endpoints

def find_paths(matrix: List[List[int]], start: Tuple[int, int], endpoints: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
    """
    Find all reachable endpoints from a starting position using BFS.
    Returns a set of reachable endpoint positions.
    """
    queue = [(start, {start})]  # (position, visited)
    reachable_endpoints = set()
    
    while queue:
        position, visited = queue.pop(0)
        
        # If we've reached an endpoint, add it to our results
        if position in endpoints:
            reachable_endpoints.add(position)
            continue
            
        # Add all valid neighbors to the queue
        for neighbor in get_valid_neighbors(matrix, position):
            if neighbor not in visited:
                new_visited = visited | {neighbor}
                queue.append((neighbor, new_visited))
    
    return reachable_endpoints

def solve_part1(data: List[str]) -> int:
    # Create the height matrix
    matrix = create_matrix(data)
    
    # Find all trailheads and endpoints
    trailheads = find_trailheads(matrix)
    endpoints = find_endpoints(matrix)
    
    # Calculate score for each trailhead
    scores = {}
    for trailhead in trailheads:
        reachable_endpoints = find_paths(matrix, trailhead, endpoints)
        scores[trailhead] = len(reachable_endpoints)
        print(f"Trailhead at {trailhead} can reach {len(reachable_endpoints)} endpoints")
    
    # Sum all scores
    total_score = sum(scores.values())
    return total_score

def main():
    # Read and process input
    # data = read_input_file()
    data = read_input_file(test_input=True)
    result = solve_part1(data)
    print(f"Sum of trailhead scores: {result}")

if __name__ == "__main__":
    main()
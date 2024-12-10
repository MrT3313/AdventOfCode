def read_input(filename):
    with open(filename) as f:
        return [[int(c) for c in line.strip()] for line in f]

def find_trailheads(grid):
    trailheads = []
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                trailheads.append((i, j))
    return trailheads

def get_neighbors(pos, grid):
    rows, cols = len(grid), len(grid[0])
    i, j = pos
    neighbors = []
    
    # Check all 4 directions
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = i + di, j + dj
        if (0 <= ni < rows and 0 <= nj < cols and 
            grid[ni][nj] == grid[i][j] + 1):
            neighbors.append((ni, nj))
    return neighbors

def count_unique_paths(grid, start):
    def dfs(pos, visited):
        if grid[pos[0]][pos[1]] == 9:
            # Convert path to tuple for hashable set
            return {tuple(visited)}
        
        paths = set()
        for next_pos in get_neighbors(pos, grid):
            if next_pos not in visited:
                # Create new path with current position
                new_visited = visited + [next_pos]
                paths.update(dfs(next_pos, new_visited))
        return paths
    
    # Start DFS from each trailhead
    return len(dfs(start, [start]))

def solve_part2(grid):
    trailheads = find_trailheads(grid)
    total = 0
    
    for start in trailheads:
        rating = count_unique_paths(grid, start)
        total += rating
        
    return total

def main():
    grid = read_input("../input.txt")
    # grid = read_input("../test_input.txt")
    result = solve_part2(grid)
    print(f"Part 2: {result}")

if __name__ == "__main__":
    main()
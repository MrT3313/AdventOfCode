def read_input(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def find_antennas(grid):
    # Dictionary to store antenna positions by frequency
    antennas = {}
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            char = grid[y][x]
            if char != '.':
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((x, y))
    return antennas

def calculate_antinodes(antennas, grid):
    antinodes = set()
    height = len(grid)
    width = len(grid[0])
    
    # For each frequency
    for freq, positions in antennas.items():
        # Check all pairs of antennas with the same frequency
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                
                # Check all points along and beyond the line between antennas
                dx = x2 - x1
                dy = y2 - y1
                
                # Check points on both sides of the antenna pair
                for t in range(-width, width*2):  # Extend search range
                    # Calculate potential antinode position
                    x = x1 + (dx * t) // max(1, abs(dx)) if dx != 0 else x1
                    y = y1 + (dy * t) // max(1, abs(dy)) if dy != 0 else y1
                    
                    # Check if point is within grid bounds
                    if 0 <= x < width and 0 <= y < height:
                        # Calculate distances to both antennas
                        dist1 = abs(x - x1) + abs(y - y1)
                        dist2 = abs(x - x2) + abs(y - y2)
                        
                        # Check if one distance is twice the other
                        if (dist1 > 0 and dist2 > 0 and 
                            (dist1 == 2 * dist2 or dist2 == 2 * dist1)):
                            antinodes.add((x, y))
    
    return antinodes

# Read the input
grid = read_input('../input.txt')
# grid = read_input('../test_input.txt')

# Find all antennas
antennas = find_antennas(grid)

# Calculate antinodes
antinodes = calculate_antinodes(antennas, grid)

# Print result
print(f"Number of unique antinode locations: {len(antinodes)}")
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

def flood_fill(matrix, row, col, char, visited):
    """Flood fill to find connected regions. Returns coordinates of region."""
    if (row < 0 or row >= len(matrix) or 
        col < 0 or col >= len(matrix[0]) or 
        matrix[row][col] != char or 
        (row, col) in visited):
        return set()
    
    visited.add((row, col))
    region = {(row, col)}
    
    # Check all 4 directions
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_region = flood_fill(matrix, row + dr, col + dc, char, visited)
        region.update(new_region)
    
    return region

def count_sides(matrix, region):
    """Count the number of distinct sides (fence sections) of a region."""
    # Track continuous horizontal and vertical fence sections
    horizontal_sections = set()
    vertical_sections = set()
    
    for row, col in region:
        # For each cell, check if it starts a new fence section
        
        # Check right side
        if (row, col + 1) not in region:
            # Find the start of this vertical section
            start_row = row
            while (start_row - 1, col) in region and (start_row - 1, col + 1) not in region:
                start_row -= 1
            vertical_sections.add((start_row, col, 'right'))
            
        # Check left side
        if (row, col - 1) not in region:
            start_row = row
            while (start_row - 1, col) in region and (start_row - 1, col - 1) not in region:
                start_row -= 1
            vertical_sections.add((start_row, col, 'left'))
            
        # Check bottom side
        if (row + 1, col) not in region:
            start_col = col
            while (row, start_col - 1) in region and (row + 1, start_col - 1) not in region:
                start_col -= 1
            horizontal_sections.add((row, start_col, 'bottom'))
            
        # Check top side
        if (row - 1, col) not in region:
            start_col = col
            while (row, start_col - 1) in region and (row - 1, start_col - 1) not in region:
                start_col -= 1
            horizontal_sections.add((row, start_col, 'top'))
    
    return len(horizontal_sections) + len(vertical_sections)

def part2(data):
    # Most of the code remains the same as part1
    matrix_height = len(data)
    matrix_width = len(data[0])

    matrix = [
        [data[row][col] for col in range(matrix_width)]
        for row in range(matrix_height)
    ]
    
    visited = set()
    regions = []
    
    for row in range(matrix_height):
        for col in range(matrix_width):
            if (row, col) not in visited:
                region = flood_fill(matrix, row, col, matrix[row][col], visited)
                if region:
                    regions.append((matrix[row][col], region))
    
    # Calculate total price using the new sides counting method
    total_price = 0
    print("\nRegion details:")
    for char, region in regions:
        area = len(region)
        sides = count_sides(matrix, region)
        price = area * sides
        total_price += price
        print(f"Region {char}: Area={area}, Sides={sides}, Price={price}")
    
    return total_price

# -- #

data = readInputFile()
# data = readInputFile(test_input=True)
result = part2(data)
print(f'THE RESULT : {result}')
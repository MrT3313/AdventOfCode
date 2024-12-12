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

def calculate_perimeter(matrix, region):
    perimeter = 0
    for row, col in region:
        # Check all 4 sides
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_row, new_col = row + dr, col + dc
            if (new_row < 0 or new_row >= len(matrix) or 
                new_col < 0 or new_col >= len(matrix[0]) or 
                (new_row, new_col) not in region):
                perimeter += 1
    return perimeter

def part1(data):
    print(f'THE DATA : {data}')
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
    print("\nOriginal matrix:")
    pprint.pprint(matrix)

    # Find all regions
    visited = set()
    regions = []
    
    for row in range(matrix_height):
        for col in range(matrix_width):
            if (row, col) not in visited:
                region = flood_fill(matrix, row, col, matrix[row][col], visited)
                if region:
                    regions.append((matrix[row][col], region))
    
    # Calculate total price
    total_price = 0
    print("\nRegion details:")
    for char, region in regions:
        area = len(region)
        perimeter = calculate_perimeter(matrix, region)
        price = area * perimeter
        total_price += price
        print(f"Region {char}: Area={area}, Perimeter={perimeter}, Price={price}")
    
    return total_price

# -- #

data = readInputFile()
# data = readInputFile(test_input=True)
result = part1(data)
print(f'THE RESULT : {result}')
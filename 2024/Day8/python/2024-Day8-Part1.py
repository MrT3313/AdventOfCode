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

def findFrequencyVectors(char_positions, matrix):
    vectors = []
    matrix_height = len(matrix)
    matrix_width = len(matrix[0])

    for char, positions in char_positions.items():
        print(f'\nChecking character: {char}')
        for i, pos1 in enumerate(positions):
            for pos2 in positions[i + 1:]:
                row1, col1 = pos1
                row2, col2 = pos2
                
                print(f"\nTesting positions: {pos1} and {pos2}")
                
                # Calculate vector components
                row_diff = row2 - row1
                col_diff = col2 - col1
                base_distance = (row_diff**2 + col_diff**2)**0.5
                if base_distance == 0:
                    continue
                
                # Normalize direction vector
                dir_row = row_diff / base_distance
                dir_col = col_diff / base_distance
                
                # Try different distances (1x, 2x, 3x, etc. of the base distance)
                for multiplier in range(1, 12):  # Reasonable limit to prevent infinite loops
                    distance = base_distance * multiplier
                    
                    # Calculate antinode positions
                    antinode1 = (
                        row1 - dir_row * (distance/2),
                        col1 - dir_col * (distance/2)
                    )
                    antinode2 = (
                        row2 + dir_row * (distance/2),
                        col2 + dir_col * (distance/2)
                    )
                    
                    print(f"Testing distance multiplier {multiplier}")
                    print(f"Antinode1: {antinode1}")
                    print(f"Antinode2: {antinode2}")
                    
                    # Validate both antinodes
                    antinodes_valid = True
                    for idx, antinode in enumerate([antinode1, antinode2]):
                        row, col = antinode
                        # Check for exact integer coordinates
                        if not (row.is_integer() and col.is_integer()):
                            print(f"Antinode {idx+1} failed: Not integer coordinates")
                            antinodes_valid = False
                            break
                            
                        # Convert to integers for bounds checking
                        row, col = int(row), int(col)
                        
                        # Check bounds and existing characters
                        # if not (0 <= row < matrix_height):
                        #     print(f"Antinode {idx+1} failed: Row out of bounds")
                        #     antinodes_valid = False
                        #     break
                        # if not (0 <= col < matrix_width):
                        #     print(f"Antinode {idx+1} failed: Column out of bounds")
                        #     antinodes_valid = False
                        #     break
                        # if matrix[row][col] != '.':
                        #     print(f"Antinode {idx+1} failed: Position not empty")
                        #     antinodes_valid = False
                        #     break
                    
                    if antinodes_valid:
                        print("Vector is valid!")
                        vectors.append({
                            'char': char,
                            'antenna1': pos1,
                            'antenna2': pos2,
                            'antinode1': (int(antinode1[0]), int(antinode1[1])),
                            'antinode2': (int(antinode2[0]), int(antinode2[1])),
                            'distance': distance
                        })
                        break  # Found a valid vector, no need to try larger multipliers
    
    return vectors
    
def part1(data):
    # VARIABLES
    matrix_height = len(data)
    matrix_width = len(data[0])
    char_positions = {}

    # CREATE: matrix
    matrix = [
        [
            data[row][col]
            for col in range(matrix_width)
        ] 
        for row in range(matrix_height)
    ]
    pprint.pprint(matrix, width=800, compact=False)
    # pprint.pprint(matrix)

    # LOOP: through matrix and get all unique frequencies (unique characters in the matrix)
    for row in range(matrix_height):
        for col in range(matrix_width):
            char = matrix[row][col]
            if char != ".":
                if char not in char_positions:
                    char_positions[char] = []
                char_positions[char].append((row, col))
    print(f'UNIQUE FREQUENCIES : {char_positions}')

    # FIND: all possible vectors between matching frequencies
    vectors = findFrequencyVectors(char_positions, matrix)
    print(f'FOUND VECTORS: {len(vectors)}')
    pprint.pprint(vectors)

    # VISUALIZE
    visualization_matrix = [row[:] for row in matrix]
    
    for vector in vectors:
        # Check both antinodes
        for antinode_key in ['antinode1', 'antinode2']:
            antinode_row, antinode_col = vector[antinode_key]
            # Check if antinode is within matrix bounds
            if (0 <= antinode_row < matrix_height and 
                0 <= antinode_col < matrix_width):
                # Round the floating point coordinates for visualization
                vis_row = antinode_row
                vis_col = antinode_col
                visualization_matrix[vis_row][vis_col] = '#'
    # pprint.pprint(visualization_matrix, width=800, compact=False)
    pprint.pprint(visualization_matrix)

    # RETURN
    count = sum(row.count('#') for row in visualization_matrix)
    return count

# -- #

data = readInputFile()
# data = readInputFile(test_input=True)
result = part1(data)
print(f'THE RESULT : {result}')

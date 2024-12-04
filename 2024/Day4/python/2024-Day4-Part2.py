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


def depthFirstSearch(matrix, row, col, matrix_height, matrix_width):
    print(f'🔄🔄🔄🔄')

    # DEBUGGING: visualize sub-matrix at this position
    sub_matrix = []
    for dx in [-1, 0, 1]:
        sub_row = []
        for dy in [-1, 0, 1]:
            new_row = row + dx
            new_col = col + dy
            
            # Check if new coordinates are within matrix boundaries
            if 0 <= new_row < matrix_height and 0 <= new_col < matrix_width:
                sub_row.append(matrix[new_row][new_col])
            else:
                sub_row.append(None)
        sub_matrix.append(sub_row)
    
    print(f'THE SUB MATRIX:')
    pprint.pprint(sub_matrix, width=40, compact=False)
    
    # CHECK: diagonal positions within sub matrix
    top_right = matrix[row - 1][col + 1] if row > 0 and col < matrix_width - 1 else None
    top_left = matrix[row - 1][col - 1] if row > 0 and col > 0 else None
    bottom_right = matrix[row + 1][col + 1] if row < matrix_height - 1 and col < matrix_width - 1 else None
    bottom_left = matrix[row + 1][col - 1] if row < matrix_height - 1 and col > 0 else None

    # CHECK: that NONE of the diagonal values are None
    if any(val is None for val in [top_right, top_left, bottom_right, bottom_left]):
        print(f'❌ Early Exit -> SUB MATRIX is on edge of MATRIX (missing row || col)')
        return 0

    # EXTRACT & CHECK: each individual single step directional
    check_1 = f'{bottom_left}{matrix[row][col]}{top_right}'
    check_1_valid = check_1 == 'MAS' or check_1 == 'SAM'
    
    check_2 = f'{top_right}{matrix[row][col]}{bottom_left}'
    check_2_valid = check_2 == 'MAS' or check_2 == 'SAM'

    check_3 = f'{top_left}{matrix[row][col]}{bottom_right}'
    check_3_valid = check_3 == 'MAS' or check_3 == 'SAM'

    check_4 = f'{bottom_right}{matrix[row][col]}{top_left}'
    check_4_valid = check_4 == 'MAS' or check_4 == 'SAM'

    if all(val is True for val in [check_1_valid, check_2_valid, check_3_valid, check_4_valid]):
        print(f'✅ FOUND PATTERN @ CENTER => ({row}, {col})')
        return 1
    else:
        print(f'❌ no pattern found @ CENTER => ({row}, {col})')
        return 0

def part1(data):
    print(f'THE DATA : {data}')

    # VARIABLES
    found_count = 0

    # EXTRACT: input dimensions
    box_height = len(data)
    box_width = len(data[0])
    print(f'BOX DIMENSIONS: ({box_height} x {box_width})')

    # CONVERT: dimensions into matrix
    matrix = [
        [
            data[row][col]
            for col in range(box_width)
        ] 
        for row in range(box_height)
    ]
    print(f'THE FULL MATRIX:')
    pprint.pprint(matrix)

    # LOOP: through matrix looking for "A"
    for row in range(box_height):
        for col in range(box_width):
            # print(f'CURRENT POSITION & CHAR : ({row},{col}) > {matrix[row][col]}')
            
            if matrix[row][col] == "A":
                print(f'"A" FOUND AT: {row}, {col}')
                word_found = depthFirstSearch(matrix, row, col, box_height, box_width)
                found_count += word_found

    print(f'TOTAL FULL WORDS FOUND: {found_count}')
    return found_count

# --------------------------------- #

data = readInputFile()
# data = readInputFile(test_input=True)
result = part1(data)
print(f'THE RESULT 🎉 : {result}')
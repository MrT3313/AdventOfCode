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


def depthFirstSearch(matrix, row, col, matrix_height, matrix_width, target_word="XMAS"):
    word_length = len(target_word)
    directions = [
        (-1, 0), (1, 0),  # Vertical (Up, Down)
        (0, -1), (0, 1),  # Horizontal (Left, Right)
        (-1, -1), (-1, 1),  # Diagonal (Up-Left, Up-Right)
        (1, -1), (1, 1)    # Diagonal (Down-Left, Down-Right)
    ]
    word_count = 0

    # LOOP: through all possible directions => looking for next letter "M"
    for dr, dc in directions:
        found_word = True

        # Iterate through each character of the target word, starting from the second letter
        # (The first letter "X" is already at the current position (row, col))
        for i in range(1, word_length):  
            # Calculate the new row and column for the i-th letter of the word
            nr, nc = row + dr * i, col + dc * i

            # BOUNDS CHECK: Ensure the new position (nr, nc) is within the matrix AND that the character at the new position matches the corresponding character in the target word.
            if not (
                0 <= nr < matrix_height and  # Row must be within matrix bounds
                0 <= nc < matrix_width       # Column must be within matrix bounds
            ) or matrix[nr][nc] != target_word[i]:  # The character must match the target
                # If either condition fails, set the flag to False and exit the inner loop as this direction cannot form the word
                found_word = False
                break

        if found_word:
            print(f'WORD "{target_word}" FOUND IN DIRECTION: {(dr, dc)} STARTING AT ({row}, {col})')
            word_count += 1
    
    return word_count


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

    # LOOP: through matrix looking for "X"
    for row in range(box_height):
        for col in range(box_width):
            print(f'CURRENT POSITION & CHAR : ({row},{col}) > {matrix[row][col]}')
            
            if matrix[row][col] == "X":
                print(f'"X" FOUND AT: {row}, {col}')
                word_found = depthFirstSearch(matrix, row, col, box_height, box_width)
                found_count += word_found

    print(f'TOTAL FULL WORDS FOUND: {found_count}')
    return found_count

# --------------------------------- #

data = readInputFile()
# data = readInputFile(test_input=True)
result = part1(data)
print(f'THE RESULT 🎉 : {result}')
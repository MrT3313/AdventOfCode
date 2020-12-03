def traverseMatrix(slope, currRow=0, currCol=0):
    # Get Input Data
    f = open("2020/Day3/Day3_input.txt", "r")
    input = f.read()
    lines = input.splitlines()
    f.close()

    # Make Matrix
    matrix = []
    for line in lines:
        matrix.append(list(line))

    # Variables
    height = len(matrix)
    width = len(matrix[0])
    count = 0

    # Loop
    while currRow < height: 
        # Get Position
        position = matrix[currRow][currCol]

        # Conditional
        if position == '#':
            count += 1

        # Increment Position
        if currCol + slope[0] >= width: 
            currCol = (currCol + slope[0]) % width
        else:
            currCol += slope[0]
        currRow += slope[1]
        
    return count

# TEST
# result = traverseMatrix(slope=(3,1)) # RIGHT 3 - DOWN 1
# print(result)
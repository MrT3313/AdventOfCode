def readInputData():
    f = open("2020/Day11/Day11_input.txt", "r")
    # f = open("2020/Day11/Day11_testData_pt1.txt", "r")
    input = f.read()
    dataArray = input.split("\n")
    f.close()

    return [_ for _ in dataArray]

def countOccupiedSeats(matrix):
    count = 0 
    for row in matrix:
        for data in row:
            if data == "#":
                count += 1
    return count

def getNeighbours(position, matrix):
    
    pool = [
        [-1, -1],    [-1, 0],    [-1, 1],
        [0, -1],                  [0, 1],
        [1, -1],     [1, 0],      [1, 1]
    ]
    numberOfNeighbours = 0
    for ringCell in pool:
        newRow = position[0] + ringCell[0]
        newCol = position[1] + ringCell[1]

        if newRow < 0 or newCol < 0:
            continue
        if newRow >= len(matrix) or newCol >= len(matrix[1]):
            continue

        newData = matrix[newRow][newCol]

        if newData == '#':
            numberOfNeighbours += 1
    
    return numberOfNeighbours

# def recurse(matrix, row=0, col=0):
def recurse(matrix, generations = []):
    # _variables_
    changes = False

    # Ceate Blank Matrix
    modifiedMatrix = [row[:] for row in matrix]

    # Loop Through Matrix
    for rowIdx, row in enumerate(matrix):
        for colIdx, col in enumerate(row):
            if col == '.': 
                continue

            neighbours = getNeighbours([rowIdx, colIdx], matrix)

            if col == 'L':
                # RULE: no occupied adjacent seats
                if neighbours == 0:
                    # UPDATE: modifiedMatrix
                    modifiedMatrix[rowIdx][colIdx] = "#"
                    changes = True
            if col == '#':
                if neighbours >= 4:
                    # UPDATE: modifiedMatrix
                    modifiedMatrix[rowIdx][colIdx] = "L"
                    changes = True
    
    # Conditional Recursion
    if changes != False:
        generations.append(modifiedMatrix)
        return recurse(modifiedMatrix, generations)
    else:
        result = countOccupiedSeats(matrix)
        return result, generations

def solve():
    # GET: data
    data = readInputData()
    # print(data)
    
    # MAKE: matrix
    matrix = []
    for line in data:
        matrix.append(list(line))

    return recurse(matrix)

# TEST
# result, generations = solve()
# print(result)
# print(generations)

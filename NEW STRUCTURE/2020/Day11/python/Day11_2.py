from Day11_1 import readInputData

def countOccupiedSeats(matrix):
  count = 0 
  for row in matrix:
    for data in row:
      if data == "#":
        count += 1
  return count

def recurseNeighbours(position, direction, matrix):
  # _variables_
  count = 0

  # CALUCLATE: new position
  newPosition = [
    position[0] + direction[0],
    position[1] + direction[1]
  ]
  # print('newPosition :', newPosition)

  # BASE CASE(s):
  ## Negative Idx
  if newPosition[0] < 0 or newPosition[1] < 0:
    return count
  ## Index out of Range
  if newPosition[0] >= len(matrix) or newPosition[1] >= len(matrix[0]):
    return count

  # GET: new position value
  newValue = matrix[newPosition[0]][newPosition[1]]
  # print('newValue :', newValue)

  # CONDITIONAL:
  if newValue == ".":
    # RECURSE:
    return recurseNeighbours(newPosition, direction, matrix)
  else:
    if newValue == '#':
      # INCREMENT: count
      count += 1
    elif newValue == 'L':
      pass
    # EXIT: current recursive direction loop
    return count

def getNeighbours(position, matrix):
  # _variables_
  directions = [
    [1, 0],   # DOWN
    [-1, 0],  # UP
    [0, 1],   # RIGHT
    [0, -1],  # LEFT
    [1, 1],   # Diag-DownRight
    [1, -1],  # Diag-DownLeft 
    [-1, 1],  # Diag-UpRight
    [-1, -1],  # Diag-UpLeft
  ]
  mainCount = 0

  # LOOP: throgh directions
  for _ in directions:
    mainCount += recurseNeighbours(position, _, matrix)

  # RETURN
  return mainCount

def recurse(matrix, generations = []):
  # _variables_
  changes = False

  # CREATE: blank matrix
  modifiedMatrix = [row[:] for row in matrix]

  # LOOP: through matrix
  for rowIdx, row in enumerate(matrix):
    for colIdx, col in enumerate(row):
      # SKIP: floor
      if col == '.':
        continue
      
      # GET: neighbours:
      neighbours = getNeighbours([rowIdx, colIdx], matrix)
      # print('neighbours :', neighbours)

      # Update: Modified Matrix
      if neighbours == 0 and matrix[rowIdx][colIdx] != '#':
        modifiedMatrix[rowIdx][colIdx] = "#"
        changes = True
      if neighbours >= 5 and matrix[rowIdx][colIdx] != 'L':
        modifiedMatrix[rowIdx][colIdx] = "L"
        changes = True
  
  # CONDITIONAL RECURSION
  if changes == True:
    generations.append(modifiedMatrix)
    return recurse(modifiedMatrix, generations)
  else:
    result = countOccupiedSeats(matrix)
    return result, generations


def solve():
  # GET: data
  data = readInputData()
  
  # CREATE: Matrix
  matrix = []
  matrix = [list(_) for _ in data]
  # print(matrix)

  # RECURSE:
  return recurse(matrix)


# TEST
result = solve()
print(result[0])
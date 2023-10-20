def getData(type = 'real'):
  f = None
  # Get Input Data
  if type == 'test':
    f = open("2021/Day9/Day9_test_input.txt", "r") # TEST DATA
  if type == 'real':
    f = open("2021/Day9/Day9_input.txt", "r") # ACTUAL DATA
  input = f.read()
  input_list = [_ for _ in input.splitlines()]
  f.close()

  return input_list

def checkAdjacent(
  matrix,
  checked_floor,
  i, j, # current position
  m, n # matrix size
):
  # variables
  adjacent_values = []

  # main logic
  checked_floor[i][j] = True
  if i > 0:
    print(matrix[i - 1][j])
    adjacent_values.append({
      'idx': (i - 1, j),
      'val': matrix[i - 1][j]
    }) 
    checked_floor[i - 1][j] = True
  if i+1 < m:
    print(matrix[i + 1][j])
    adjacent_values.append({
      'idx': (i + 1, j),
      'val': matrix[i + 1][j]
    }) 
    checked_floor[i + 1][j] = True
  if j > 0:
    print(matrix[i][j - 1])
    adjacent_values.append({
      'idx': (i, j - 1),
      'val': matrix[i][j - 1]
    }) 
    checked_floor[i][j - 1] = True
  if j+1 < n:
    print(matrix[i][j + 1])
    adjacent_values.append({
      'idx': (i, j + 1),
      'val': matrix[i][j + 1]
    })
    checked_floor[i][j + 1] = True
  
  adjacent_values.sort(key=lambda x: x['val'])
  if adjacent_values[0]['val'] < matrix[i][j]:
    return adjacent_values[0], checked_floor
  else: 
    return True, checked_floor

def calculateRisk(min_idxs,  matrix):
  total_risk = 0
  for _ in min_idxs:
    total_risk += matrix[_[0]][_[1]] + 1

  return total_risk


def smokeBasin():
  # input_list = getData('test')
  input_list = getData()

  # variables
  minimums = set()


  # make sea floor
  sea_floor = [[int(_) for _ in row] for row in input_list]
  checked_floor = [[False for _ in row] for row in input_list]

  # loop through matrix
  for i in range(len(sea_floor)):
    for j in range(len(sea_floor[0])):
      # check adjacent values
      check_result, checked_floor = checkAdjacent(
        sea_floor,
        checked_floor,
        i, j,
        len(sea_floor),
        len(sea_floor[0])
      )

      if check_result == True:
        if sea_floor[i][j] != 9:
          print('Adding Min Value', i, '-', j, sea_floor[i][j])
          minimums.add((i, j))

  return calculateRisk(minimums, sea_floor)




# TEST
result = smokeBasin()
print(result)
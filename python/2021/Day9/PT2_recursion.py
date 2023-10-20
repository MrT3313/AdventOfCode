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

def adjacent_idxs(
  matrix,
  i, j, # current position
  m, n, # matrix size
):
  # check params
  # print('Current Position', i, j, '-', matrix[i][j])
  # print('Matrix Size', m, n)
  # variables
  adjacent = []

  # main logic
  if i > 0:
    # print(matrix[i - 1][j])
    adjacent.append((i - 1, j)) 
  if i+1 < m:
    # print(matrix[i + 1][j])
    adjacent.append((i + 1, j)) 
  if j > 0:
    # print(matrix[i][j - 1])
    adjacent.append((i, j - 1)) 
  if j+1 < n:
    # print(matrix[i][j + 1])
    adjacent.append((i, j + 1))
  
  return adjacent

def recurse(
  matrix,
  i, j, # current position
  m, n, # matrix size
  checked_floor,
  curr_basin_num,
  seen_set,
  curr_basin = {
    'size': 0,
    'idxs': []
  },
  target_val = 9,
):
  print('SEEN SET', type(seen_set),seen_set)
  print('RECURSION', i, ',', j, ':', matrix[i][j], checked_floor[i][j])
  # BASE CASE
  check_str = f'{i}{j}'
  print('CHECK STRING',check_str)
  if check_str in seen_set:
    print('WE HIT A BASE CASE - 1')
    return curr_basin, checked_floor, seen_set
  if matrix[i][j] == target_val:
    print('WE HIT A BASE CASE - 2')
    checked_floor[i][j] = "!"
    return curr_basin, checked_floor, seen_set 
  if checked_floor[i][j] != -1:
    print('WE HIT A BASE CASE - 3')
    checked_floor[i][j] = curr_basin_num
    return curr_basin, checked_floor, seen_set
  ## ?? add logic for is checked_floor value != False

  # CURRENT POINT LOGIC
  curr_basin['size'] += 1
  curr_basin['idxs'].append((i,j))
  checked_floor[i][j] = curr_basin_num
  print('--',type(seen_set))
  seen_set.add(f'{i}{j}')

  # ADJACENT
  adjacent = adjacent_idxs(  
    matrix,
    i, j, # current position
    m, n, # matrix size
  )
  print(adjacent)
  # filter adjacent
  # for _ in adjacent:
  #   if _ not in seen_set:


  for _ in matrix:
    print(_)
  for _ in checked_floor:
    print(_)

  # RECURSE
  print("Current Basin Before Recurse", curr_basin)
  filtered_adjacent = [y for y in adjacent if f'{y[0]}{y[1]}' not in seen_set]
  print('FILTERING ADJACENT', seen_set)
  print('FILTERED ADJACENT', filtered_adjacent)
  print('')
  print('')
  # for _ in adjacent:
  for _ in filtered_adjacent:
    print('CURRENT RECURSION :) 👉', _)
    return recurse(
      matrix,
      _[0], _[1],
      m, n,
      checked_floor,
      curr_basin_num,
      seen_set,
      curr_basin,
    )


def smokeBasin():
  input_list = getData('test')
  # input_list = getData()

  # make sea floor
  sea_floor = [[int(_) for _ in row] for row in input_list]
  checked_floor = [[-1 for _ in row] for row in input_list]
  seen_set = set()
  print(type(seen_set),seen_set)

  # loop through matrix
  basins_found = 0
  baisns = []
  for i in range(len(sea_floor)):
    for j in range(len(sea_floor[0])):
      if checked_floor[i][j] != -1: continue
      if f'{i}{j}' in seen_set: continue
      
      # check adjacent values
      curr_basin, checked_floor, seen_set = recurse(
        sea_floor,
        i, j, # current position
        len(sea_floor), len(sea_floor[0]),
        checked_floor,
        basins_found,
        seen_set
      )
      print('')
      print('')
      print('CHUNK: curr_basin', curr_basin)
      print('CHUNK: checked_floor')
      for _ in sea_floor:
        print(_)
      for _ in checked_floor:
        print(_)
      print('CHUNK: seen_set', seen_set)

      baisns.append(curr_basin)
      basins_found += 1
  
  print('')
  print('')
  baisns.sort(key=lambda x: x['size'])
  print('BASINS FOUND', basins_found)
  print('THE BASINS - length', len(baisns))
  print('THE BASINS - first', baisns[0])
  print('THE BASINS - last', baisns[len(baisns) - 1])
  print('THE CHECKED FLOOR', checked_floor)
  return




# TEST
result = smokeBasin()
print(result)
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

def smokeBasin():
  input_list = getData('test')
  # input_list = getData()

  # make sea floor
  sea_floor = [[int(_) for _ in row] for row in input_list]
  checked_floor = [[-1 for _ in row] for row in input_list]
  seen_set = set()
  print(type(seen_set),seen_set)

  # loop through matrix
  # basins_found = 0
  # baisns = []
  for i in range(len(sea_floor)):
    for j in range(len(sea_floor[0])):
      if checked_floor[i][j] != -1: continue
      if f'{i}{j}' in seen_set: continue
      
      # get adjacent
      adjacent = adjacent_idxs(
        sea_floor,
        i, j, # current position
        len(sea_floor), len(sea_floor[0]) # matrix size
      )
      adjacent.append((i,j))
      print('FIRST MAIN LOOP ADJACENT', adjacent)
      filtered_adjacent = [_ for _ in adjacent if f'{adjacent[0]}{adjacent[1]}' not in seen_set]
      print('SEEN SET', seen_set)
      print('FIRST MAIN LOOP FILTERED ADJACENT', filtered_adjacent)

  
      print('POINTS - 1', filtered_adjacent)

      basins_found = 0
      while len(filtered_adjacent) != 0:
        curr_idx = filtered_adjacent.pop()
        print('CURRENT IDX', curr_idx)



        seen_set.add(f'{curr_idx[0]}{curr_idx[1]}')

        print('')
        print('')

      print('!!')
      print('!!')
      basins_found += 1




  
  # print('')
  # print('')
  # baisns.sort(key=lambda x: x['size'])
  # print('BASINS FOUND', basins_found)
  # print('THE BASINS - length', len(baisns))
  # print('THE BASINS - first', baisns[0])
  # print('THE BASINS - last', baisns[len(baisns) - 1])
  # print('THE CHECKED FLOOR', checked_floor)
  return




# TEST
result = smokeBasin()
print(result)
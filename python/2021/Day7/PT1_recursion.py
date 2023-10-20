# 
# This approach hits the max recursion limit on the real data
#

import statistics

def getData(type = 'real'):
  f = None
  # Get Input Data
  if type == 'test':
    f = open("2021/Day7/Day7_test_input.txt", "r") # TEST DATA
  if type == 'real':
    f = open("2021/Day7/Day7_input.txt", "r") # ACTUAL DATA
  input = f.read()
  input_list = [int(_) for _ in input.split(',')]
  f.close()

  return input_list

def recurse(arr, curr_num, min, max, direction, result = []):
  # BASE CASE
  if direction == "up" and curr_num > max:
    return result
  if direction == "down" and curr_num < min:
    return result

  # logic
  loop_distance = [0 for _ in arr]
  # calcualte loop distance
  for idx, _ in enumerate(arr):
    loop_distance[idx] = abs(curr_num - _)
  # calculate total loop distance sum
  loop_distance_sum = sum(loop_distance)
  # append result
  result.append({
    'num': curr_num,
    'loop_distanct': loop_distance,
    'sum': loop_distance_sum,
  })

  # increment
  if direction == "up" and curr_num <= max:
    curr_num = curr_num + 1
  if direction == "down" and curr_num >= min:
    curr_num = curr_num - 1

  # recurse
  return recurse(arr, curr_num, min, max, direction, result)

def findBest(arr):
  best = {}
  for idx, _ in enumerate(arr):
    if idx == 0:
      best = _
    else:
      if _['sum'] < best['sum']:
        best = _

  return best

def theTreacheryOfWhales():
  # input_list = getData('test')
  input_list = getData()
  input_list.sort()
  print(len(input_list), input_list)

  mean = statistics.mean(input_list)
  print(type(mean), mean)

  median = int(round(statistics.median(input_list), 0))
  print(type(median), median)

  direction = None
  if mean > median:
    direction = 'up'
  else:
    direction = 'down'


  calculation = recurse(
    input_list,
    median,                   # start
    input_list[0],                      # min
    input_list[len(input_list) - 1],    # max
    direction,
  )

  return findBest(calculation)


# TEST
result = theTreacheryOfWhales()
print(result)
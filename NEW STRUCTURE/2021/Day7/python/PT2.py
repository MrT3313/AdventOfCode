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

  # VARIABLES
  mean = statistics.mean(input_list)
  curr_num = int(round(statistics.median(input_list), 0))
  direction = None
  if mean > curr_num:
    direction = 'up'
  else:
    direction = 'down'
  min = input_list[0]
  max = input_list[len(input_list) - 1]
  result = []

  while (
    direction == 'up' and curr_num <= max
  ) or (
    direction == 'down' and curr_num >= min
  ): 
    # logic
    loop_distance = [0 for _ in input_list]
    # loop_distance_total = [0 for _ in input_list]

    # calcualte loop distance
    for idx, _ in enumerate(input_list):
      loop_distance[idx] = abs(curr_num - _)
    
    # calculate total loop distance sum
    loop_distance_sum = 0

    for _ in loop_distance:
      loop_distance_sum += sum([num for num in range(_ + 1)])
    
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

  return findBest(result)


# TEST
result = theTreacheryOfWhales()
print('THE BEST RESULT', result)
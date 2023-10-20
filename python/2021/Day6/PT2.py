def getData():
  # Get Input Data
  # f = open("2021/Day6/Day6_1_test_input.txt", "r") # ACTUAL DATA
  f = open("2021/Day6/Day6_input.txt", "r") # ACTUAL DATA
  input = f.read()
  input_list = [int(_) for _ in input.split(',')]
  f.close()

  return input_list

def lanternFish():
  fish = getData()

  # VARIABLES
  count = [0 for _ in range(9)]
  end = 256
  loop = 0

  # get initial count
  for _ in fish:
    count[_] = count[_] + 1

  while loop < end:
    new_count = [0 for _ in range(9)]
    # loop through current days fish
    for idx, _ in enumerate(count):
      if idx == 0:
        # add new fish
        new_count[8] = 1 * _
        # reset birthing fish
        new_count[6] = 1 * _
      else:
        # decrement fish days
        new_count[idx - 1] = new_count[idx - 1] + count[idx] 

    count = new_count
    # increment loop
    loop += 1
  
  return sum(count) 

# TEST
result = lanternFish()
print(result)
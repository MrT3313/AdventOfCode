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
  days = 80
  loop = 0

  while loop < days:
    new_fish = []
    # loop through current days fish
    for idx, _ in enumerate(fish):
      if _ == 0:
        # add new fish an dreset birthing fish
        fish[idx] = 6
        new_fish.append(8)
      else:
        # decrement fish days
        fish[idx] -= 1
    
    # append new fish to next days fish
    fish = fish + new_fish
    # increment loop
    loop += 1
  
  return len(fish)

# TEST
result = lanternFish()
print(result)


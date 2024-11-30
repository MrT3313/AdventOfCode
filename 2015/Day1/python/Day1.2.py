def part1():
  # Get Input Data
  f = open("2015/Day1/input.txt", "r")
  data = f.read()
  instructions = list(data)
  f.close()
  
  # variables
  floor = 0
  idx = 0

  # loop over all instructions
  while idx < len(instructions):
    command = instructions[idx]

    # ☝️ || 👇
    if (command == "("):
      floor += 1
    if (command == ")"):
      floor -= 1
    
    # escape case
    if (floor == -1):
      return idx + 1

    # increment pointer
    idx += 1

result = part1()
print('Entering Basement IDX', result)
def part1():
  # Get Input Data
  f = open("2015/Day1/input.txt", "r")
  data = f.read()
  instructions = list(data)
  f.close()

  floor = 0
  idx = 0

  while idx < len(instructions):
    command = instructions[idx]

    if (command == "("):
      floor += 1
    if (command == ")"):
      floor -= 1

    idx += 1
  
  return floor

result = part1()
print('THE FINAL FLOOR', result)
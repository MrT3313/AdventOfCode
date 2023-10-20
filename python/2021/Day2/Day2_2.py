def dive():
  # Get Input Data
  f = open("2021/Day2/Day2_input.txt", "r")
  input = f.read()
  input_list = [_ for _ in input.splitlines()]
  f.close()

  # VARIABLES
  horizontal = 0
  depth = 0
  aim = 0

  # FUNCTIONS
  def decreaseAim(aim, val):
    aim -= val
    return aim
  def increaseAim(aim, val):
    aim += val
    return aim
  def moveForward(aim, curr_x, curr_y, val):
    curr_x += val
    curr_y += val * aim
    return curr_x, curr_y
  movement = {
    "up": decreaseAim,
    "down": increaseAim,
    "forward": moveForward
  }

  # LOOP
  for command in input_list:
    # split command
    split = command.split()

    if split[0] == "up":
      aim = movement['up'](aim, int(split[1]))
    if split[0] == "down":
      aim = movement['down'](aim, int(split[1]))
    if split[0] == "forward":
      horizontal, depth = movement['forward'](aim, horizontal, depth, int(split[1]))


  # Final Multiplication
  result = depth * horizontal
  return result 

# TEST
result = dive()
print(result)
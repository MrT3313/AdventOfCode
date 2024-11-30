def dive():
  # Get Input Data
  f = open("2021/Day2/Day2_input.txt", "r")
  input = f.read()
  input_list = [_ for _ in input.splitlines()]
  f.close()

  # VARIABLES
  horizontal = 0
  depth = 0

  # FUNCTIONS
  def decreaseDepth(curr_y, val):
    curr_y -= val
    return curr_y
  def increaseDepth(curr_y, val):
    curr_y += val
    return curr_y
  def moveForward(curr_x, val):
    curr_x += val
    return curr_x
  movement = {
    "up": decreaseDepth,
    "down": increaseDepth,
    "forward": moveForward
  }

  # LOOP
  for command in input_list:
    # split command
    split = command.split()

    if split[0] == "up":
      depth = movement['up'](depth, int(split[1]))
    if split[0] == "down":
      depth = movement['down'](depth, int(split[1]))
    if split[0] == "forward":
      horizontal = movement['forward'](horizontal, int(split[1]))


  # Final Multiplication
  result = depth * horizontal
  return result

# TEST
result = dive()
print(result)
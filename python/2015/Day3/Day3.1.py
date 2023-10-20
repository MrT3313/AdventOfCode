def updateLocation(x,y):
  return [f"{x},{y}", x, y]

def deliverPackage(grid, location):
  print('placing package at this location', location)
  
  [locationString, grid_x, grid_y] = location
  print('WHAT IS THIE', locationString)

  if locationString in grid:
    print('Key exists')
    grid[locationString] = grid[locationString] + 1
  else:
    print('Key does not exist')
    grid[locationString] = 1

  return grid

def move(currentLocation, movementDirection):
  
  [locationString, x, y] = currentLocation

  if (movementDirection == "UP"):
    print('MOVING UP')
    return updateLocation(x, y + 1)
  if (movementDirection == "DOWN"):
    print('MOVING DOWN')
    return updateLocation(x, y - 1)
  if (movementDirection == "RIGHT"):
    print('MOVING RIGHT')
    return updateLocation(x + 1, y)
  if (movementDirection == "LEFT"):
    print('MOVING LEFT')
    return updateLocation(x - 1, y)

def part1():
  # Get Input Data
  f = open("2015/Day3/input.txt", "r")
  data = f.read()
  instructions = list(data)
  f.close()

  # print(instructions)

  # location
  location = updateLocation(0,0)

  # generate grid and place initial package
  grid = { location[0] : 1 }

  # loop through instructions
  pointer = 0
  while pointer < len(instructions):
    print('')
    print('')
    
    current_instruction = instructions[pointer]
    print('THE CURRENT INSTRUCTION', current_instruction)

    movement = None
    if (current_instruction == "^"): movement = "UP"
    if (current_instruction == "v"): movement = "DOWN"
    if (current_instruction == "<"): movement = "LEFT"
    if (current_instruction == ">"): movement = "RIGHT"

    print('=> THE MOVEMENT', movement)

    location = move(location, movement)
    print('=> THE NEW LOCATION', location)
    grid = deliverPackage(grid, location)

    pointer += 1  
  
  return grid



result = part1()
print(len(result))
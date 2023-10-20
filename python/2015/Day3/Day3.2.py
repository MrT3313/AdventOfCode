def updateLocation(x,y):
  return [f"{x},{y}", x, y]

def deliverPackage(grid, location):
  print('placing package at this location', location)
  
  [locationString, grid_x, grid_y] = location

  if locationString in grid:
    print('INITIAL grid value', grid[locationString])
    grid[locationString] = grid[locationString] + 1
  else:
    print('first time at this location')
    grid[locationString] = 1

  print('NEW grid value', grid[locationString])

  return grid

def move(currentLocation, movementDirection):
  
  [locationString, x, y] = currentLocation

  if (movementDirection == "UP"):
    return updateLocation(x, y + 1)
  if (movementDirection == "DOWN"):
    return updateLocation(x, y - 1)
  if (movementDirection == "RIGHT"):
    return updateLocation(x + 1, y)
  if (movementDirection == "LEFT"):
    return updateLocation(x - 1, y)

def getMovementDirection(current_instruction):
  if (current_instruction == "^"): return "UP"
  if (current_instruction == "v"): return "DOWN"
  if (current_instruction == "<"): return "LEFT"
  if (current_instruction == ">"): return "RIGHT"

def part2():
  ## ASSUMPTION: even list -> each person needs an instruction in each iteration

  # Get Input Data
  f = open("2015/Day3/input.txt", "r")
  data = f.read()
  instructions = list(data)
  f.close()

  # TESTS
  # instructions = list('^v^v^v^v^v') # 11
  # instructions = list('^>v<') # 3

  # location
  santaLocation = updateLocation(0,0)
  botLocation = updateLocation(0,0)

  # generate grid and place initial package
  grid = { santaLocation[0] : 2 }

  # loop through instructions
  pointer = 0
  while pointer + 1 < len(instructions):
    print('')
    print('')
    
    current_instruction = [
      instructions[pointer], 
      instructions[pointer + 1]
    ]
    # print('THE CURRENT INSTRUCTION', current_instruction)

    # get movement directions
    santaMovement = getMovementDirection(current_instruction[0])
    botMovement = getMovementDirection(current_instruction[1])
    # print('SANTA MOVEMENT', santaMovement, 'BOT MOVEMENT', botMovement)

    # move
    santaLocation = move(santaLocation, santaMovement)
    botLocation = move(botLocation, botMovement)
    # print('SANTA LOCATION', santaLocation, 'BOT LOCATION', botLocation)

    # deliver packages
    grid = deliverPackage(grid, santaLocation)
    grid = deliverPackage(grid, botLocation)
    # print('THE NEW GRID', grid)

    pointer += 2 
  
  return grid



result = part2()
print(len(result))
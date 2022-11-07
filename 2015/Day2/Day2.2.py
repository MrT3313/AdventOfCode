def part1():
  # Get Input Data
  f = open("2015/Day2/input.txt", "r")
  input = f.read()
  boxes = [ line.split('x') for line in input.splitlines()]
  f.close()

  # paper needed
  ## 2*l*w + 2*w*h + 2*h*l
  ## + the area of the smallest side

  totalWrappingPaper = 0
  totalRibbon = 0

  for box in boxes:
    l = int(box[0])
    w = int(box[1])
    h = int(box[2])

    # calcualte box values
    surface_area = calculateSurfaceArea(l,w,h)
    smallest_side = calculateSmallestSide(l,w,h)

    ribbon_length = calculateRibbonLength(l,w,h)
    bow_length = calculateBowLength(l,w,h)

    # update accumulators
    totalWrappingPaper += surface_area + smallest_side
    totalRibbon += ribbon_length + bow_length

  return [totalWrappingPaper, totalRibbon]

# HELPER FUNCTIONS #
def calculateSurfaceArea(l,w,h):
  return (2*l*w) + (2*w*h) + (2*h*l) 
def calculateSmallestSide(l,w,h):
  arr = [l*w, w*h, h*l]
  arr.sort()
  return arr[0]
def calculateRibbonLength(l,w,h):
  arr = [l,w,h]
  arr.sort()
  return (2 * arr[0]) + (2*arr[1])
def calculateBowLength(l,w,h):
  return l*w*h


# TEST #
result = part1()
print('Total Wrapping Paper', result[0])
print('Total Ribbon', result[1])
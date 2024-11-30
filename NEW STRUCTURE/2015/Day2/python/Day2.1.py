def part1():
  # Get Input Data
  f = open("2015/Day2/input.txt", "r")
  input = f.read()
  boxes = [ line.split('x') for line in input.splitlines()]
  f.close()

  # paper needed
  ## 2*l*w + 2*w*h + 2*h*l
  ## + the area of the smallest side

  total = 0

  for box in boxes:
    l = int(box[0])
    w = int(box[1])
    h = int(box[2])

    surface_area = calculateSurfaceArea(l,w,h)
    smallest_side = calculateSmallestSide(l,w,h)

    total += surface_area + smallest_side

  return total

# HELPER FUNCTIONS #
def calculateSurfaceArea(l,w,h):
  return (2*l*w) + (2*w*h) + (2*h*l) 
def calculateSmallestSide(l,w,h):
  arr = [l*w, w*h, h*l]
  arr.sort()
  return arr[0]

# TEST #
print(part1())
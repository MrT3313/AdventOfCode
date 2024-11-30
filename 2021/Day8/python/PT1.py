def getData(type = 'real'):
  f = None
  # Get Input Data
  if type == 'test':
    f = open("2021/Day8/Day8_test_input.txt", "r") # TEST DATA
  if type == 'real':
    f = open("2021/Day8/Day8_input.txt", "r") # ACTUAL DATA
  input = f.read()
  input_list = [_.split(' | ') for _ in input.splitlines()]
  f.close()

  return input_list

def sevenSegmentSearch():
  # input_list = getData('test')
  input_list = getData()

  # -- NOTES --
  #  aaaa
  # b    c
  # b    c
  #  dddd  
  # e    f
  # e    f
  #  gggg 
  # a = TOP Horizontal
    # b = TOP LEFT Vertical
    # c = TOP RIGHT VERTICAL
  # d = MIDDLE Horizontal
    # e = BOTTOM LEFT Vertical
    # f = BOTTOM RIGHT Vertical
  # g = BOTTOM Horizontal

  # SINGLE inputs across a - g "wires"

  # each 3 digit display is mixed up differently 

  # LEFT of input string (array[0]) is the noted signal pattern
  # RIGHT of input string (array[1]) is the triggered 4 digit output

  count = 0
  for line in input_list:
    for digit in line[1].split(' '):
      if len(digit) in [2, 3, 4, 7]:
        count += 1
  
  return count


# TEST
result = sevenSegmentSearch()
print(result)
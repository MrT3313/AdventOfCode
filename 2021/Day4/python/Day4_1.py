## -- HELPER FUNCTIONS -- ##
def createBoard(rowCount, colCount, list):
  board = []
  for i in range(rowCount):
    rowList = []
    for j in range(colCount):
      rowList.append(list[rowCount * i + j])
    board.append(rowList)

  return board

def updateBoard(b, val):
  # update board if passed value is a match
  for i in range(len(b[0])):
    for j in range(len(b[i])):
      # check for matching value
      if b[i][j] == val:
        b[i][j] = True
  # check for winning board
  winner = True if checkForWinner(b) else False
  # return
  if winner:
    return True, b
  else:
    return False, b

def checkForWinner(b):
  # check rows for winner
  for i in range(len(b[0])):
    winner = all(_ is True for _ in b[i])
    if winner:
      return True

  # check columns for winner
  for i in range(len(b)):
    column = []
    for j in range(len(b[i])):
      column.append(b[j][i])
    winner = all(_ is True for _ in column)
    if winner:
      return True
  
  return False
      
def calculateSum(b, winning_num):
  total = 0
  for i in range(len(b[0])):
    for j in range(len(b[i])):
      if b[i][j] != True:
        total += b[i][j]

  return total * winning_num

## -- MAIN FUNCTION -- ##
def giantSquid():
  # Get Input Data
  f = open("2021/Day4/Day4_input.txt", "r")
  input = f.read()
  input_list = [_ for _ in input.split("\n\n")]
  f.close()

  # extract numbers to be called
  nums = [int(_) for _ in input_list.pop(0).split(',')]
  
  # create boards
  boards = []
  for row in input_list:
    split_row = [int(_) for _ in row.split()]
    boards.append(createBoard(5, 5, split_row))

  # WINNING VARIABLES
  winningBoard = False
  winningNum = False
  
  # loop through nums
  while len(nums) > 0 and winningBoard == False:
    # get current number
    curr_num = nums.pop(0)

    # loop through all boards
    for b in boards:
      result, b = updateBoard(b, curr_num)
      if result:
        winningBoard = b
        winningNum = curr_num
        break

  print('THE WINNING BOARD', winningBoard)
  return calculateSum(winningBoard, winningNum)

# Test
result = giantSquid()
print(result)
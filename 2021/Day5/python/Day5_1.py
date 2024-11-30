def hydrothermalVenture():
  # Get Input Data
  # f = open("2021/Day5/Day5_input.txt", "r") # ACTUAL DATA
  f = open("2021/Day5/Day5_test_input.txt", "r") # TEST DATA
  input = f.read()
  input_list = [_ for _ in input.splitlines()]
  f.close()

  # make sea floor
  # sea_floor = [[0 for _ in range(1000)] for _ in range(1000)] # ACTUAL DATA
  sea_floor = [[0 for _ in range(10)] for _ in range(10)] # TEST DATA
  # print(sea_floor) # DONT PRINT ON REAL DATA - 1,000,000 ROWS: IT WILL FREEZE

  # variables
  num_of_overlaps = 0

  for _ in input_list:
    # split coords
    split = _.split('->')
    p1_x_str, p1_y_str = split[0].strip().split(',')
    p2_x_str, p2_y_str = split[1].strip().split(',')
    p1_x = int(p1_x_str)
    p1_y = int(p1_y_str)
    p2_x = int(p2_x_str)
    p2_y = int(p2_y_str)

    # check for horizontal
    if p1_y == p2_y:
      print('HORIZONTAL LINE')
      print('P1', p1_x, p1_y)
      print('P2', p2_x, p2_y)

      # extract row
      row = p1_y

      # update columns
      curr_col = min(p1_x, p2_x)
      while curr_col <= max(p1_x, p2_x):
        if sea_floor[row][curr_col] == 0:
          sea_floor[row][curr_col] = 1
        else:
          # check if first overlap
          if sea_floor[row][curr_col] == 1:
            num_of_overlaps += 1
          # update sea floor
          sea_floor[row][curr_col] += 1

        # increment current col
        curr_col += 1

      print(sea_floor) # DONT PRINT ON REAL DATA - 1,000,000 ROWS: IT WILL FREEZE

    elif p1_x == p2_x: 
      print('VERTICAL LINE')
      print('P1', p1_x, p1_y)
      print('P2', p2_x, p2_y)

      # extract col
      col = p1_x

      # update rows
      curr_row = min(p1_y, p2_y)
      while curr_row <= max(p1_y, p2_y):
        if sea_floor[curr_row][col] == 0:
          sea_floor[curr_row][col] = 1
        else:
          # check if first overlap
          if sea_floor[curr_row][col] == 1:
            num_of_overlaps += 1
          # update sea floor
          sea_floor[curr_row][col] += 1

        # increment curr row
        curr_row += 1

      print(sea_floor) # DONT PRINT ON REAL DATA - 1,000,000 ROWS: IT WILL FREEZE
    else:
      print('DIAGONAL LINE')
      
      print(sea_floor) # DONT PRINT ON REAL DATA - 1,000,000 ROWS: IT WILL FREEZE
    print('')
    print('')

  print(sea_floor) # DONT PRINT ON REAL DATA - 1,000,000 ROWS: IT WILL FREEZE
  return num_of_overlaps

# TEST
result = hydrothermalVenture()
print(result)
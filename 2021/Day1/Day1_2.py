## STANDARD LOOP
def sliding_window():
  # Get Input Data
  f = open("2021/Day1/Day1_input.txt", "r")
  input = f.read()
  input_list = [int(_) for _ in input.splitlines()]
  f.close()

  # Variables
  window_size = 3
  start = 0
  end = start + window_size
  n = 0
  increase = 0
  decrease = 0

  # get first window
  prev_window = input_list[start : end]

  while n < len(input_list) - 3:
    # get next window
    start += 1
    end += 1
    current_window = input_list[start : end]

    # calculate
    prev_total = sum(prev_window)
    curr_total = sum(current_window)

    # compare
    if curr_total > prev_total:
      increase += 1
    if curr_total < prev_total:
      decrease += 1

    # increment
    prev_window = current_window
    n += 1
  
  # return
  return increase, decrease

# TEST
result = sliding_window()
print(result)
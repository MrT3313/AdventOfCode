# inspiration: https://www.reddit.com/r/adventofcode/comments/rbvpui/2021_day_8_part_2_my_logic_on_paper_i_used_python/

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
    
  # generate output array
  output = [[None for _ in range(4)] for line in input_list]

  for line_idx, line in enumerate(input_list):
    # LOOP VARIABLES
    signal_map = {}
    curr_signals = line[0]
    curr_digits = line[1]

    ##### -- LOOP 1 : decode unique inputs -- #####
    for signal in curr_signals.split(' '):
      # sort string alphabetically
      sorted_signal = sorted(signal)
      sorted_signal_string = ''.join(sorted_signal)

      # map unique digits
      if len(signal) == 2:
        signal_map[sorted_signal_string] = 1
      if len(signal) == 3:
        signal_map[sorted_signal_string] = 7
      if len(signal) == 4:
        signal_map[sorted_signal_string] = 4
      if len(signal) == 7:
        signal_map[sorted_signal_string] = 8

    # isolate the 'L' in 4
    key_list = list(signal_map.keys())
    value_list = list(signal_map.values())
    position_4 = value_list.index(4)
    position_1 = value_list.index(1)
    key_4 = key_list[position_4]
    key_1 = key_list[position_1]
    four_dif = []
    for _ in [_ for _ in key_4]:
      if _ not in [_ for _ in key_1]:
        four_dif.append(_)
    four_dif.sort()

    ##### -- LOOP 2 : decode remaining digits -- #####
    for digit_idx, digit in enumerate(curr_digits.split(' ')):
      # sort string alphabetically
      sorted_digit = sorted(digit)
      sorted_digit_string = ''.join(sorted_digit)

      if sorted_digit_string in signal_map:
        output[line_idx][digit_idx] = signal_map[sorted_digit_string]
      else:
        if len(sorted_digit_string) == 5:
          # looking for: 2 || 3 || 5

          # find key of 1
          # looking for "back bone" of 3 which matches 1
          key_list = list(signal_map.keys())
          value_list = list(signal_map.values())
          position = value_list.index(1)
          key_1 = key_list[position]
          split_key_1 = [_ for _ in key_1]

          if all(elem in sorted_digit for elem in split_key_1):
            # THIS IS A 3
            signal_map[sorted_digit_string] = 3
            output[line_idx][digit_idx] = signal_map[sorted_digit_string]
          elif all(elem in sorted_digit for elem in four_dif):
            # 'THIS IS A 5
            signal_map[sorted_digit_string] = 5
            output[line_idx][digit_idx] = signal_map[sorted_digit_string]
          else:
            # THIS IS A 2
            signal_map[sorted_digit_string] = 2
            output[line_idx][digit_idx] = signal_map[sorted_digit_string]
          
        if len(sorted_digit_string) == 6:
          # looking for: 0 || 6 || 9

          # find key of 4
          key_list = list(signal_map.keys())
          value_list = list(signal_map.values())
          position = value_list.index(4)
          key_4 = key_list[position]
          split_key_4 = [_ for _ in key_4]

          if all(elem in sorted_digit for elem in split_key_4):
            # THIS IS A 9
            signal_map[sorted_digit_string] = 9
            output[line_idx][digit_idx] = signal_map[sorted_digit_string]
          elif all(elem in sorted_digit for elem in four_dif):
            # THIS IS A 6
            signal_map[sorted_digit_string] = 6
            output[line_idx][digit_idx] = signal_map[sorted_digit_string]
          else:
            # THIS IS A 0
            signal_map[sorted_digit_string] = 0
            output[line_idx][digit_idx] = signal_map[sorted_digit_string]

  return sum(
    [
      int(
        ''.join(
          [str(int) for int in _]
        )
      ) for _ in output]
  )


# TEST
result = sevenSegmentSearch()
print(result)
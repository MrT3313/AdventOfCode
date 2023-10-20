## STANDARD LOOP
def sonarSweep():
  # Get Input Data
  f = open("2021/Day1/Day1_input.txt", "r")
  input = f.read()
  input_list = [int(_) for _ in input.splitlines()]
  f.close()

  increase = 0
  decrease = 0

  prev = int(input_list.pop(0))

  for idx, val in enumerate(input_list):
    # Logic
    if val > prev:
      increase += 1
    if val < prev:
      decrease += 1

    # Reset Prev
    prev = val
  
  return increase, decrease

# TEST
result = sonarSweep()
print(result)
# define recursive function
def recurse(type, list, col_idx = 0):
  # 1 Calculate New Threwhold
  threshold = len(list) // 2

  # 2 Find Primary & Secondary Values
  sorted_list = sorted(list, key= lambda x: x[col_idx])
  primary = 0 if sorted_list[threshold][col_idx] == str(0) else 1
  secondary = 1 if primary == 0 else 0

  # 3 Filter invalid numvers
  if type == 'oxygen':
    filtered_list = [x for x in sorted_list if int(x[col_idx]) == primary]
  if type == 'co2':
    filtered_list = [x for x in sorted_list if int(x[col_idx]) == secondary]
  
  # BASE CASE
  if len(filtered_list) == 1:
    return filtered_list[0]
  
  # 4 Recurse 
  return recurse(type, filtered_list, col_idx + 1) 

def BinaryDiagnostic():
  # Get Input Data
  f = open("2021/Day3/Day3_input.txt", "r")
  input = f.read()
  input_list = [_ for _ in input.splitlines()]
  f.close()

  # -- PSUDO -- #
  # 1. Calculate New Threwhold
  # 2. Find Primary & Secondary Values
  # 3. Filter invalid numvers
  # 4. Recurse

  # get values
  oxygen = recurse('oxygen', input_list)
  c02 = recurse('co2', input_list)
  # convert binary string to int
  oxygen_binary_int = int(oxygen, 2)
  co2_binary_int = int(c02, 2)

  return oxygen_binary_int * co2_binary_int


# Test
result = BinaryDiagnostic()
print(result)
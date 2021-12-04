def BinaryDiagnostic():
  # Get Input Data
  f = open("2021/Day3/Day3_input.txt", "r")
  input = f.read()
  input_list = [_ for _ in input.splitlines()]
  f.close()

  # threshold needed to determine the most common bit value
  threshold = len(input_list) // 2
  val_length = len(input_list[0])

  # VARIABLES
  gamma_rate = []
  epsilon_rate = []

  for col_idx in range(0, val_length): 
    # sort list
    sorted_list = sorted(input_list, key= lambda x: x[col_idx])

    # check 500th element @ appropriate column index
    primary = 0 if sorted_list[threshold][col_idx] == str(0) else 1
    secondary = 1 if primary == 0 else 0

    # append values
    gamma_rate.append(primary)
    epsilon_rate.append(secondary)

  # convert to list of strings
  gamma_s = [str(i) for i in gamma_rate]
  epsilon_s = [str(i) for i in epsilon_rate]
  # join to single string
  gamma_binary = ''.join(gamma_s)
  epsilon_binary = ''.join(epsilon_s)
  # convert from binary string to int
  gamma_binary_int = int(gamma_binary, 2)
  epsilon_binary_int = int(epsilon_binary, 2)

  return gamma_binary_int * epsilon_binary_int

# Test
result = BinaryDiagnostic()
print(result)
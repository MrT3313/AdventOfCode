def part1():
  # Get Input Data
  f = open("2022/Day1/Day1_input.txt", "r")
  input = f.read()
  lines = input.splitlines()
  f.close()

  result = {
    "total": float('-inf'),
    "elf_number": None
  }
  currentElfTotal = 0
  num = 0
  for line in lines:

    print('THIS LINE', line)

    if line != "":
      print('adding new line', currentElfTotal, int(line))
      currentElfTotal += int(line)
    else:
      print('calculating total', currentElfTotal, result)
      if currentElfTotal > result['total']:
        result['total'] = currentElfTotal
        result['elf_number'] = num

      currentElfTotal = 0
      num += 1

      print('UPDATED total', currentElfTotal, result)
      print('')
      print('')
  
  return result

result = part1()
print('RESULT', result)
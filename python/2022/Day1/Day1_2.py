def part1():
  # Get Input Data
  f = open("2022/Day1/Day1_input.txt", "r")
  input = f.read()
  lines = input.splitlines()
  f.close()

  top3 = [
    {
      "total": float('-inf'),
      "elf_number": None
    }, 
    {
      "total": float('-inf'),
      "elf_number": None
    }, 
    {
      "total": float('-inf'),
      "elf_number": None
    }
  ]
  currentElfTotal = 0
  num = 0
  for line in lines:

    print('THIS LINE', line)

    if line != "":
      print('adding new line', currentElfTotal, int(line))
      currentElfTotal += int(line)
    else:
      print('calculating total', currentElfTotal, top3)

      currElf = {
        "total": currentElfTotal,
        "elf_number": num
      }
      
      # 1
      if currentElfTotal > top3[0]['total']:
        
        # add new first element
        top3.insert(0, currElf)
        print('here1', top3)
        # remove last element
        top3.pop()

      # 2
      elif currentElfTotal > top3[1]['total']:
        print('here2')
        
        # insert new element
        top3.insert(1, currElf)
        # remove last element
        top3.pop()

      # 3
      elif currentElfTotal > top3[2]['total']:
        print('here3')

        # remove last element
        top3.pop()
        # replace last element
        top3.append(currElf)

      ## RESET ##
      currentElfTotal = 0
      num += 1

      for el in top3:
        print('=> el', el)
      print('')
      print('')
  
  result = 0
  for blarg in top3:
    result += blarg["total"]

  return result

result = part1()
print('RESULT', result)
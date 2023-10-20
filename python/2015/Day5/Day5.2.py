
def isNice1(str):
  dict = {}

  pointer = 0

  while pointer < len(str):
    # check for uplicated pairing
    if f'{str[pointer]},{str[pointer + 1]}' in dict:
      # make sure first pointer does not overlap
      testValues = dict[f'{str[pointer]},{str[pointer + 1]}']

      if pointer not in testValues: 
        # prevent out of index error
        if pointer + 2 <= len(str):
          # make sure second pointer does not overlap
          if pointer + 2 not in testValues:
            return True
    else:
      dict[f'{str[pointer]},{str[pointer + 1]}'] = [pointer, pointer + 1]

    if pointer + 2 == len(str):
      return False
    pointer += 1

  return False

def isNice2(str):
  pointer = 0

  while pointer < len(str) - 1:
    if str[pointer] == str[pointer + 2]:
      return True

    if pointer + 3 == len(str):
       return False
    pointer += 1
  
  return False

def isNice(str):
  res1 = isNice1(str)
  res2 = isNice2(str)

  result = True
  if False in [res1, res2]:
    result = False

  return result

def part2():
  # Get Input Data
  f = open("2015/Day5/input.txt", "r")
  input = f.read()
  lines = input.splitlines()
  f.close()

  # TEST
  # lines = [
  #   "qjhvhtzxzqqjkmpb",
  #   "xxyxx",
  #   "uurcxstgmygtbstg",
  #   "ieodomkazucvgmuy",
  # ]

  niceLines = []
  naughtyLines = []

  for line in lines:
    nice = isNice(line)
    if nice:
      niceLines.append(line)
    else:
      naughtyLines.append(line)

  return [niceLines, naughtyLines]



result = part2()
print(len(result[0]))

def isNice1(str):
  # contains at least 4 vowels
  strList = list(str)
  vowelCount = 0

  for el in enumerate(strList):
    if el[1] in ["a", "e", "i", "o", "u"]:
      if vowelCount + 1 == 3: 
        return True
      vowelCount += 1

  # if we get here - its false
  return False

def isNice2(str):
  pointer = 0

  while pointer < len(str):
    # check for duplicates
    if str[pointer] == str[pointer + 1]:
      return True

    if pointer + 2 >= len(str):
      return False

    pointer += 1

  return False

def isBannedString(str):
  pointer = 0

  while pointer < len(str):
    currString = f'{str[pointer]}{str[pointer + 1]}'

    if currString in ['ab','cd','pq','xy']:
      return True

    if pointer + 2 >= len(str):
      return False

    pointer += 1

  return False
    

def isNice(str):
  res1 = isNice1(str)
  res2 = isNice2(str)

  res3 = isBannedString(str)
  
  result = True
  if False in [res1, res2]:
    result = False 
  
  if True in [res3]:
    return False

  return result

def part1():
  # Get Input Data
  f = open("2015/Day5/input.txt", "r")
  input = f.read()
  lines = input.splitlines()
  f.close()

  # TEST
  # lines = [
  #   "ugknbfddgicrmopn",   # nice
  #   "aaa",                # nice
  #   "jchzalrnumimnmhp",   # naughty - no double
  #   "haegwjzuvuyypxyu",   # naughty - string xy
  #   "dvszwmarrgswjxmb"    # naughty - only 1 vowel
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



result = part1()
print(len(result[0]))
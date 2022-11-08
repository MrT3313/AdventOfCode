import hashlib

def part1():
  # Get Input Data
  f = open("2015/Day4/input.txt", "r")
  seed = f.read()
  f.close()

  # TEST
  # seed = 'abcdef'
  # string = f'{seed}609043'
  # seed = 'pqrstuv'
  # string = f'{seed}1048970'
  # return hashlib.md5(string.encode()).hexdigest()

  curr = ['z' for el in range(5)]

  result = [None, None] # [hash, seed]
  i = 0

  result = ''.join(str(e) for e in curr)

  while result[:5] != '00000':
    string = f'{seed}{i}'
    result = hashlib.md5(string.encode()).hexdigest()
    print(f'{i}-{seed}-🐙-{result[:5]}--{result}')
    i += 1

  return [result, seed, i - 1]

result = part1()
print(result)
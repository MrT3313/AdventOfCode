def getData(type = 'real'):
  f = None
  # Get Input Data
  if type == 'test':
    f = open("2021/Day10/Day10_test_input.txt", "r") # TEST DATA
  if type == 'real':
    f = open("2021/Day10/Day10_input.txt", "r") # ACTUAL DATA
  input = f.read()
  input_list = [[char for char in _] for _ in input.splitlines()]
  f.close()

  return input_list

def processLine(line, closing_pair, opening_pair):

    chunk = []
    for str_idx, char in enumerate(line):
        print('-- str_idx : current_char---', str_idx, ':', char)
        print('--- line ---', line)
        print('--- chunk ---', chunk)

        if char in closing_pair:
            chunk.append(char)
        else:
            check = chunk[len(chunk) - 1]
            pair = opening_pair[char]

            if pair == check:
                chunk.pop()

        print('')
    

    return chunk, line

    

def syntaxScoring():
    input_lines = getData()
    # input_lines = getData('test')

    points = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }

    closing_pair = {
        '<': '>',
        '[': ']',
        '{': '}',
        '(': ')',
    }
    opening_pair = {
        ">": "<",
        ']': '[',
        '}': '{',
        ')': '(',
    }

    final = []
    for line_num, _ in enumerate(input_lines):
        total = 0
        print(line_num, _)

        result, line = processLine(_, closing_pair, opening_pair)
        print('LINE', line)
        print('LINE RESULT', result)
        print('')
        print('')
        
        total = 0
        for char in reversed(result):
            print('CURRENT CHAR', char)

            x5 = total * 5
            new_points = points[closing_pair[char]]
            print('x5', type(x5), x5)
            print('new_points', type(new_points), new_points)
            total = x5
            print('NEW TOTAL - 1', type(total), total)
            total += new_points
            print('NEW TOTAL - 2', type(total), total)
        
        final.append({
            'chunk': result,
            'total': total
        })
    

    final.sort(key=lambda x: x['total'])
    print('FINAL')
    for _ in final:
        print(_)

    print(len(final))
    mid = len(final) // 2
    print('MID POINT', mid)

    return final[mid]
    



# TEST
result = syntaxScoring()
print(result)
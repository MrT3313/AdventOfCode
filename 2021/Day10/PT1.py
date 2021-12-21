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

def processLine(line):
    print('')
    print('')
    print('NEW LINE')
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
    error_lookup = {
        ')': 3, 
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    # search_idx = -1
    chunk = []
    invalid = []
    for str_idx, char in enumerate(line):
        print('-- str_idx : current_char---', str_idx, ':', char)
        print('--- line ---', line)
        print('--- chunk ---', chunk)
        if char in closing_pair:
            # print('OPENING')
            chunk.append(char)  
            # search_idx += 1 
            
        else:
            # print('LOOKING FOR MATCHING OPENING PAIR')

            # check = line[search_idx]
            check = chunk[len(chunk) - 1]
            pair = opening_pair[char]

            if pair == check:
                print('FOUND PAIR')
                # search_idx -= 1
                chunk.pop()
            else:
                print('NOT FOUND PAIR')
                print('ILLIGAL CHARACTER')

                invalid.append({
                    "char": char,
                    "error": error_lookup[char]
                })
                # search_idx += 1
        print('')
        print('')

    #### FULL LINE TOTAL ####
    # total = 0
    # print('LINE INVALID - Current Total', total)
    # for _ in invalid:
    #     print('!_!_!',_)
    #     # Calculate Total
    #     total += _['error']
    
    # if len(invalid) == 0:
    #     return 0
    # else:
    #     print('CURRENT ERROR', invalid[0]['error'])
    #     return total
    # total = 0


    #### FIRST ITEM ####    
    if len(invalid) == 0:
        print('NO INVALID')
        return 0
    else:
        print('CURRENT ERROR', invalid[0])
        print('CURRENT ERROR', invalid[0]['error'])
        return invalid[0]['error']

def syntaxScoring():
    input_list = getData()
    # input_list = getData('test')

    print('INPUT LENGTH', len(input_list))
    total = 0
    for _ in input_list:
        print('CURRENT LINE', type(_), _)
        curr_chunk = []
        print('CURRENT CHUNK', curr_chunk)
        
        line_result = processLine(_)
        print('CONTINUE', line_result)
        print('-!!-')
        total += line_result









    return  total

# TEST
result = syntaxScoring()
print('RESULT:', result)
import pprint

def readInputFile(test_input=False):
    if test_input:
        f = open("../test_input.txt", "r")
    else:
        f = open("../input.txt", "r")

    line = f.read()
    f.close()

    return line

def processLine(line):
    # VARIABLES
    result = []
    file_idx = 0

    # LOOP: through line
    for index, char in enumerate(line):
        if (index % 2 == 0):
            # PROCESS > file
            # print(f'...processing file...\n\tFile Index : {file_idx}\n\tChar : {line[index]}')

            # CONFIGURE: repititions
            repetitions = int(char)

            # APPEND: dynamic result
            result.extend([file_idx] * repetitions)

            # INCREMENT > file index
            file_idx += 1
        else:
            # PROCESS > free space
            # print(f'...processing free space...\n\tChar : {line[index]}')

            # CONFIGURE: repititions
            repetitions = int(char)

            # APPEND: dynamic result
            result.extend("." * repetitions)

    return result

def squishLine(list):
    # VARIABLES
    debug_processing_print = 0
    
    # GROUP: numbers by file ID
    file_groups = {}
    for i, val in enumerate(list):
        if isinstance(val, int):
            if val not in file_groups:
                file_groups[val] = []
            file_groups[val].append(i)
    
    # PROCESS: files in descending order
    for file_id in sorted(file_groups.keys(), reverse=True):
        positions = file_groups[file_id]
        file_size = len(positions)
        
        # FIND: leftmost valid space "."
        current_start = min(positions)
        best_start = current_start
        
        # LOOK: for spaces before the current position
        for i in range(current_start):
            if all(list[j] == '.' for j in range(i, i + file_size)):
                best_start = i
                break
        
        # MOVE: file IF we found a better position
        if best_start < current_start:
            # REMOVE: old positions
            for pos in positions:
                list[pos] = '.'
            
            # INSERT: in new position
            for offset in range(file_size):
                list[best_start + offset] = file_id
                
        if debug_processing_print % 100 == 0:
            print(f'...squishing line : {debug_processing_print}...')
        debug_processing_print += 1
    
    return list

def checksum(list):
    total = 0
    for position, value in enumerate(list):
        # Skip free spaces ('.')
        if isinstance(value, int):
            total += position * value
    return total

def part1(line):
    new_line = processLine(line)
    print(f'PROCESSED LINE : {new_line}')

    new_new_line = squishLine(new_line)
    print(f'SQUASHED LINE : {new_new_line}')

    return checksum(new_new_line)

# -- #

data = readInputFile()
# data = readInputFile(test_input=True)
result = part1(data)
print(f'THE RESULT : {result}')
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

    # LOOP
    while True:
        # FIND: first '.' index
        first_dot_index = list.index('.') if '.' in list else -1

        # FIND: last digit index
        last_number_index = -1
        for i in range(len(list) - 1, -1, -1):
            if isinstance(list[i], int):
                last_number_index = i
                break

        # IF: 
        #   we can't find both a dot and a number, 
        #   or if the dot is after the number,
        # THEN: 
        #   we're done processing
        if (
            first_dot_index == -1 or 
            last_number_index == -1 or 
            first_dot_index > last_number_index
        ):
            break

        # SWAP: elements in place
        list[first_dot_index], list[last_number_index] = list[last_number_index], list[first_dot_index]

        # INCREMENT: debugging print
        if (debug_processing_print % 5 == 0):
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
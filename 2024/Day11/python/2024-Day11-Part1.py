import pprint

def readInputFile(test_input=False):
    if test_input:
        f = open("../test_input.txt", "r")
    else:
        f = open("../input.txt", "r")

    data = f.read()
    lines = data.splitlines()
    f.close()

    return list(map(int, lines[0].split()))

def part1(data, num_of_blinks=25):
    '''
        EXAMPLE:
            Input: 0 1 10 99 999
            Output (after 1 blink): 1 2024 1 0 9 9 2021976
    '''
    # CHANGES -> "according to the first application rule" in this list
        # NOTES:
            # NO leading zeros
                # split 1000 
                    # left = 10
                    # right = 0
        # RULES:
            # 0 => replaced by stone / 1
            # even number of digits => replaced by 2 stones
                # left half of digits => left stone
                # right half of the digits => right stone
            # ELSE => old num * 2024

    print(f'THE DATA : {data}')

    # VARIABLES
    blink_count = 1
    while blink_count <= num_of_blinks:
        # VARIABLES
        new_data = []

        print(f'CURRENT BLINK COUNT : {blink_count} / {num_of_blinks} > {len(data)}')

        for index, num in enumerate(data):
            # print(f'\tCURRENT INPUT INDEX : {index}')
            # print(f'\tCURRENT NUM : {num}')

            if data[index] == 0:
                # print(f'\t_A_')
                # SWAP: 0 to 1
                new_data.append(1)
            elif len(str(data[index])) % 2 == 0:
                # print(f'\t_B_')
                # SPLIT: current number is half based on digit length => 1000 turns into 10 & 00
                num_str = str(data[index])
                # print(f'\tCURRENT NUM STRING : {num_str}')

                mid = len(num_str) // 2
                left_half = int(num_str[:mid]) # int conversion strips leading zeros
                right_half = int(num_str[mid:]) # int conversion strips leading zeros
                # print(f'\t\tLEFT SPLIT : {left_half}')
                # print(f'\t\tRIGHT SPLIT : {right_half}')

                new_data.append(left_half)
                new_data.append(right_half) 
            else:
                # print(f'\t\t_C_')
                new_data.append(data[index] * 2024)

            # print(f'\n\t\t{new_data}\n')


        # INCREMENT
        data = new_data
        # print(f'\tAFTER BLINK {blink_count}:\n\t {data}')
        blink_count += 1


    
    return len(data)

# -- #

data = readInputFile()
# data = readInputFile(test_input=True)
# PT1
# result = part1(data, num_of_blinks=25)
# PT2
result = part1(data, num_of_blinks=75)
print(f'THE RESULT : {result}')
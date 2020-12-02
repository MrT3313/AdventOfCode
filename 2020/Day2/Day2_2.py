def validPasswords_charPosition():
    # Get Input Data
    f = open("2020/Day2/Day2_input.txt", "r")
    input = f.read()
    input_list = input.splitlines()
    f.close()

    # Variables
    validPasswords = 0

    # Loop through each policy and password
    for idx, line in enumerate(input_list):
        # Split line into its component parts
        splitLine = line.split(' ')
        # [0] = positions
        # [1] = letter
        # [2] = password

        # Variables / Prep Data
        limits = splitLine[0].split('-')

        idx1 = int(limits[0]) - 1
        idx2 = int(limits[1]) - 1
        letter = splitLine[1][0]  

        # Check Positions
        if splitLine[2][idx1] == letter and splitLine[2][idx2] == letter:
            continue
        elif splitLine[2][idx1] == letter or splitLine[2][idx2] == letter:
            validPasswords += 1

    # RETURN
    return validPasswords

result = validPasswords_charPosition()
print(result)
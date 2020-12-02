def validPasswords_charCount():
    # Get Input Data
    f = open("2020/Day2/Day2_input.txt", "r")
    input = f.read()
    input_list = input.splitlines()
    f.close()

    # Variables
    validPasswords = 0

    # Loop through each policy and password
    for line in input_list:
        # Split line into its component parts
        splitLine = line.split(' ')
        # [0] = limit
        # [1] = letter
        # [2] = password

        # Variables / Prep Data
        limits = splitLine[0].split('-')

        limitMin = int(limits[0])
        limitMax = int(limits[1])
        letter = splitLine[1][0]
        count = 0    

        # Loop through password
        for char in splitLine[2]:
            if char == letter:
                count += 1

        # Conditional
        if count >= limitMin and count <= limitMax:
            validPasswords += 1
    
    # RETURN
    return validPasswords

result = validPasswords_charCount()
print(result)
    
def twoNumberSum(target = 2020):
    # Get Input Data
    f = open("2020/Day1/Day1_input.txt", "r")
    input = f.read()
    input_list = [int(_) for _ in input.splitlines()]
    f.close()

    # Variables
    seenData = set()

    # Loop
    for num in input_list:
        # Calcualte New Target
        newTarget = target - num

        # Check if we are already passed the New Target
        if newTarget in seenData:
            return num * newTarget
        # Add Number to seedData set before continuing to loop
        else: 
            seenData.add(num)

    # Target not found
    return False

result = twoNumberSum()
print(result)
    
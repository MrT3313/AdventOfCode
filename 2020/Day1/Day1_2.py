def threeNumberSum(target = 2020):
    # Get Input Data
    f = open("2020/Day1/Day1_input.txt", "r")
    input = f.read()
    input_list = [int(_) for _ in input.splitlines()]
    f.close()

    # Sort List
    input_list.sort()

    # Loop through each individual number
    for idx, num in enumerate(input_list):
        # Edge Case
        if idx == len(input_list) - 2: 
            break

        # Variables
        leftIdx = idx + 1
        rightIdx = len(input_list) - 1

        # While Loop until pointers cross
        while leftIdx < rightIdx:
            # Calculate Total
            currentTotal = num + input_list[leftIdx] + input_list[rightIdx]

            # Conditional
            if currentTotal == target:
                return num * input_list[leftIdx] * input_list[rightIdx]
            elif currentTotal > target:
                # Move RIGHT pointer
                rightIdx -= 1
            else:
                # move LEFT pointer
                leftIdx += 1

    return False


result = threeNumberSum()
print(result)
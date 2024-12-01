import re

def readInputFile():
    f = open("../input.txt", "r")
    data = f.read()
    lines = data.splitlines()
    f.close()
    return lines

def part2():
    # VARIABLES
    array1 = []
    array2 = []
    similarity_score = []
    result = None

    # GET: input data
    lines = readInputFile()

    # SPLIT: each line into its left and right arrays
    for line in lines:
        parts = re.split(r'\s{3}', line)  # Split the line by 3 spaces
        array1.append(parts[0].strip())
        array2.append(parts[1].strip())

    # COUNT: number instances in array2
    array2_number_counts = {
        num: array2.count(num) for num in sorted(set(array2))
    }

    # LOOP: through right list
    for lNum in array1:
        similarity_score.append(
            int(lNum) * int(array2_number_counts.get(lNum, 0))
        )

    # SUM: similarity score array
    result = sum(similarity_score)

    # RETURN
    return result

result = part2()

print(f'THE RESULT 🎉: {result}') # Answer: 25358365
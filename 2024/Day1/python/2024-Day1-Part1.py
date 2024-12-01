import re

def readInputFile():
	f = open("../input.txt", "r")
	data = f.read()
	lines = data.splitlines()
	f.close()
	return lines

def part1():
	# VARIABLES
	array1 = []
	array2 = []
	diffArray = []
	result = None

	# GET: input data
	lines = readInputFile()

	# SPLIT: each line into its left and right arrays
	for line in lines:
		parts = re.split(r'\s{3}', line)  # Split the line by 3 spaces 
		array1.append(parts[0].strip())  
		array2.append(parts[1].strip())

	# SORT: each array MIN to MAX
	array1.sort()
	array2.sort()

	# CALCULATE: difference
	if (len(array1) != len(array2)):
		print(f'ERROR: incongruent input lengths')
		return result
	else:
		for n in range(len(array1)):
			diffArray.append(
				abs(
					int(array1[n]) - int(array2[n])
				)
			)

	# SUM: diff array
	result = sum(diffArray)

	# RETURN
	return result

result = part1()
print(f'THE RESULT 🎉: {result}') # Answer: 2580760

def readInputFile():
	with open("../input.txt", "r") as f:
	# with open("../test_input.txt", "r") as f:
		lines = [
			# 1. Convert the split parts of the line into integers
			list(map(int, 
				# 2. Split the line into a list of space-separated substrings
				line.split()
			))  
			# 3. Loop through each line in the file content split into lines
			for line in f.read().splitlines()
		]
	return lines


def part1():
	# VARIABLES
	safeLineIdx = []
	unsafeLineIdx = []
	velocityThresholdInclusiveMin = 1
	velocityThresholdInclusiveMax = 3

	# GET: input data
	lines = readInputFile()
	
	# LOOP: through all lines
	for index, line in enumerate(lines):
		# VARIABLES
		currNumIdx = 1
		prevNumIdx = currNumIdx - 1
		direction = None
		valid = True

		while currNumIdx < len(line):
			# CONFIGURE: line direction
			if (currNumIdx == 1):
				if (line[currNumIdx] > line[prevNumIdx]):
					direction = 'UP'
				elif (line[currNumIdx] < line[prevNumIdx]):
					direction = 'DOWN'
				else:
					valid = False
					unsafeLineIdx.append(index)
					break

			# CHECK: direction
			if (
				(direction == "UP" and (line[currNumIdx] < line[prevNumIdx])) or
				(direction == "DOWN" and (line[currNumIdx] > line[prevNumIdx]))
			):
				valid = False
				unsafeLineIdx.append(index)
				break

			# CHECK: velocity
			velocity = abs(line[currNumIdx] - line[prevNumIdx])
			if (
				velocity > velocityThresholdInclusiveMax or
				velocity < velocityThresholdInclusiveMin
			):
				valid = False
				unsafeLineIdx.append(index)
				break
		
			# INCREMENT
			prevNumIdx += 1
			currNumIdx += 1

		if (valid):
			safeLineIdx.append(index)

	return {
		"safe": {
			"data": safeLineIdx,
			"length": len(safeLineIdx)
		},
		"unsafe": {
			"data": unsafeLineIdx,
			"length": len(unsafeLineIdx)
		}
	}

result = part1()
print(f'🎉 RESULT: {result["safe"]["length"]}')

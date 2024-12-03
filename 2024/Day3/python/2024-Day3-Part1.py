def readInputFile(test_input=False):
	if (test_input == True):
		f = open("../test_input.txt", "r")
	else:
		f = open("../input.txt", "r")

	data = f.read()
	lines = data.splitlines()
	f.close()

	return lines

def to_single_line(input_string):
	return ''.join(input_string.splitlines())

def remove_whitespace(input_string):
	return input_string.replace(" ", "").replace("\t", "").replace("\n", "").replace("\r", "")

valid_internal_characters = ["0","1","2","3","4","5","6","7","8","9",","]

def part1(data):
	# VARIABLES
	extracted_multiplications = []
	multiplied_results = []

	# JOIN: the list into a single string
	combined_data = ''.join(data)

	# REMOVE: white space
	clean_data = remove_whitespace(combined_data)

	# LOOP: through each character in combined string
	index = 0
	while index < len(clean_data):
		# print(f'CURRENT INDEX : {index}')
		# print(f'CURRENT CHAR : {clean_data[index]}')

		if clean_data[index:index + 4] == "mul(":
			# UPDATE: index to skip "mul("
			index += 4

			# SET: current starting point to check internal bracket "(" ")" values
			curr_start = index
			curr_end = index

			# FIND: ending bracket
			while curr_end < len(clean_data) and clean_data[curr_end] != ")":
				curr_end += 1

			# EXTRACT: internal content
			if curr_end < len(clean_data) and clean_data[curr_end] == ")":
				internal_content = clean_data[curr_start:curr_end]

				# CHECK: internal content contains only valid characters
				if all(char in valid_internal_characters for char in internal_content):
					extracted_multiplications.append(internal_content)

					try:
						num1, num2 = map(int, internal_content.split(','))
						multiplication_result = num1 * num2
						multiplied_results.append(multiplication_result)
					except ValueError:
						print(f'INVALID CONTENT (non-integer values found): {internal_content}')

		# Increment index
		index += 1

	return sum(multiplied_results)

# --------------------------------- #

data = readInputFile()
result = part1(data)
print(f'THE RESULT 🎉 : {result}')
    
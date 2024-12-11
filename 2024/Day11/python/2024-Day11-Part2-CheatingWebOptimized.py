from collections import defaultdict

'''
Order of stones does not matter, so represent stones as a dictionary with the
key being the stone number and the value being the count of stones with that
number.

This representation can be directly transformed into a representation of the
next generation of stones, and scales with unique numbers represented among
the stones rather than with the total stone count.
'''

def read_file(filename):
	with open(filename) as file:
		stones = list(map(int, file.read().strip().split()))
		stones_dict = defaultdict(int)
		for stone in stones:
			stones_dict[stone] += 1
		return stones_dict
		
def blink(stones_dict):
	'''
	Given an intial set of stones represented by stones_dict return a
	dict representing the set of stones after one blink.
	'''
	new_stones_dict = defaultdict(int)
	for stone, count in stones_dict.items():
		for new_stone in transform(stone):
			new_stones_dict[new_stone] += count
	return new_stones_dict
		
def blink_n_times(stones_dict, n):
	'''
	Given an intial set of stones represented by stones_dict return a
	dict representing the set of stones after n blinks.
	'''	
	for _ in range(n):
		stones_dict = blink(stones_dict)
	return stones_dict
	
def transform(stone_number):
	'''
	Given a stone number, returns a list of numbers that the stone transforms to
	after a blink.
	'''
	new_stone_numbers = []
	if stone_number == 0:
		new_stone_numbers.append(1)
	else:
		stone_str = str(stone_number)
		num_digits = len(stone_str)
		if num_digits & 1 == 0: # check for even
			half_digits = num_digits >> 1 # divide by two
			new_stone_numbers.append(int(stone_str[:half_digits]))
			new_stone_numbers.append(int(stone_str[half_digits:]))
		else:
			new_stone_numbers.append(stone_number*2024)
	return new_stone_numbers

stones_dict = read_file("../input.txt")
print(sum(blink_n_times(stones_dict, 75).values()))
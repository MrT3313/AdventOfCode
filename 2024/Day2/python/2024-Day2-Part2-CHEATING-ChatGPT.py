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

def is_safe_report(levels):
    '''
        This function checks if the 'levels' list is either strictly increasing or strictly decreasing, and if the difference between any two adjacent levels is between 1 and 3 (inclusive).
    '''
    
    # Check if the levels are strictly increasing with differences between 1 and 3.
    # This will iterate through the levels, comparing each level with the next one.
    increasing = all(1 <= (levels[i+1] - levels[i]) <= 3 for i in range(len(levels) - 1))
    # Explanation:
    # - (levels[i+1] - levels[i]): Finds the difference between two adjacent levels.
    # - 1 <= ... <= 3: Ensures the difference is between 1 and 3, inclusive.
    # - all(...): Returns True only if all comparisons in the list comprehension are True.
    #   So it ensures every adjacent difference is between 1 and 3 in an increasing order.

    # Check if the levels are strictly decreasing with differences between 1 and 3.
    # This will iterate through the levels, comparing each level with the next one (but in reverse).
    decreasing = all(1 <= (levels[i] - levels[i+1]) <= 3 for i in range(len(levels) - 1))
    # Explanation:
    # - (levels[i] - levels[i+1]): Finds the difference between two adjacent levels (reverse direction).
    # - 1 <= ... <= 3: Ensures the difference is between 1 and 3, inclusive.
    # - all(...): Returns True only if all comparisons in the list comprehension are True.
    #   So it ensures every adjacent difference is between 1 and 3 in a decreasing order.

    # Return True if the levels are either strictly increasing or strictly decreasing.
    # This is based on whether either of the conditions ('increasing' or 'decreasing') holds true.
    return (increasing or decreasing)
    # Explanation:
    # - The function returns True if either the 'increasing' condition or the 'decreasing' condition is True.
    # - If neither condition is met (i.e., the levels are neither strictly increasing nor strictly decreasing),
    #   the function will return False.

def check_report(levels):
    # If the report is already safe, return True
    if is_safe_report(levels):
        return True
    
    # If the report is unsafe, check by removing one level
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i+1:]
        if is_safe_report(modified_levels):
            return True
    
    # If no valid modification made it safe, return False
    return False

def count_safe_reports(data):
    safe_reports_count = 0
    for report in data:
        if check_report(report):  # Since the data is already a list of integers, no need for extra conversion
            safe_reports_count += 1
    return safe_reports_count

# Read the input data from the file
reports = readInputFile()

# Count safe reports with the Problem Dampener
print(count_safe_reports(reports))  # Output will be the count of safe reports
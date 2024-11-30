import os
import re

def part1():
  # Print the current working directory
  print("Current Working Directory:", os.getcwd())

  # Assuming the script is in the same directory as the input file
  path = "input.txt"
  cleaned_lines = []  # Initialize an empty list to store cleaned lines
  running_total = 0

  try:
    with open(path, "r") as f:
      for line in f:
        cleaned_line = re.sub(r'[^0-9]', '', line)
        cleaned_lines.append(cleaned_line)  # Append the cleaned line to the list
  except FileNotFoundError as e:
    print(f"Error opening file: {e}")

  for num_str in cleaned_lines:
    if (len(num_str) == 0):
      print('EMPTY STRING')
    elif (len(num_str) == 1):
      running_total += int(num_str * 2)
    elif (len(num_str) > 1):
      first_char = num_str[0]
      last_char = num_str[-1]
      running_total += int(first_char + last_char)

  return running_total

result = part1()
print('THE FINAL - 2023 Day 1 (Python) - RESULT', result)


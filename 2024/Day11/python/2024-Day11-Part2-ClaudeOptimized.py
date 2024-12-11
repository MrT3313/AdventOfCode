from collections import deque
import math

def readInputFile(test_input=False):
    filename = "../test_input.txt" if test_input else "../input.txt"
    with open(filename) as f:
        return [int(x) for x in f.readline().split()]

def part1_optimized(data, num_of_blinks=25):
    """
    Optimized version of the blinking function with the following improvements:
    1. Uses deque instead of list for O(1) append operations
    2. Avoids string conversions where possible
    3. Uses math operations instead of string manipulation
    4. Minimizes memory allocations
    """
    # Pre-calculate 2024 multiplier
    MULTIPLIER = 2024
    
    # Use deque for O(1) append operations
    current = deque(data)
    
    for blink in range(num_of_blinks):
        print(f'{blink} / {num_of_blinks} : {len(current)}')
        
        next_state = deque()
        
        while current:
            num = current.popleft()
            
            if num == 0:
                # Rule 1: 0 becomes 1
                next_state.append(1)
                continue
                
            # Calculate number of digits without string conversion
            if num == 0:
                digits = 1
            else:
                digits = math.floor(math.log10(abs(num))) + 1
            
            if digits % 2 == 0:
                # Rule 2: Even number of digits - split into two
                divisor = 10 ** (digits // 2)
                left = num // divisor
                right = num % divisor
                next_state.append(left)
                next_state.append(right)
            else:
                # Rule 3: Multiply by 2024
                next_state.append(num * MULTIPLIER)
        
        current = next_state
    
    return len(current)

# --- #

data = readInputFile()
result = part1_optimized(data, num_of_blinks=75)
print(f'THE RESULT: {result}')
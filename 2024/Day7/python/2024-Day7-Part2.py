def readInputFile(test_input=False):
    if test_input:
        f = open("../test_input.txt", "r")
    else:
        f = open("../input.txt", "r")

    data = f.read()
    lines = data.splitlines()
    f.close()

    return lines

available_operators = ["*", "+", "||"]

def part1(data):
    print(f'THE DATA : {data}')

    valid_equations = []
    invalid_equations = []

    print(f'\n\n')
    for line in data:
        print(f'THE CURRENT LINE : {line}')

        # SEPARATE: target from input
        [target, input] = line.split(':')
        target = int(target)

        # CONVERT: input into array
        input_array = []
        for token in input.split():
            input_array.append(int(token))
            input_array.append(None)
        input_array.pop()

        # Process the line recursively
        result = find_valid_equation(input_array.copy(), target)
        if result:
            # print(f'VALID LINE : {line}')
            valid_equations.append(line)
        else:
            # print(f'INVALID LINE : {line}')
            invalid_equations.append(line)
        print(f'=====')
        print(f'=====\n\n')

    return sum(int(equation.split(':')[0]) for equation in valid_equations)

def find_valid_equation(equation, target):
    # FIND: first None value
    try:
        none_index = equation.index(None)
    except ValueError:
        # CALCULATE: final result => No more None values
        result = calculate_equation(equation) == target
        print(f'FINAL EQUATION CHECK: {equation} = {calculate_equation(equation)} (Target: {target}) -> {result}')
        return result
    print(f'1st None Index : {none_index}')

    # TRY: each operator at the current position
    for operator in available_operators:
        print(f'CURRENT OPERATOR : {operator}')
        # CREATE: copy of equation with the current operator
        new_equation = equation.copy()
        new_equation[none_index] = operator
        
        # RECURSE
        result = find_valid_equation(new_equation, target)
        if result:  # If we found a valid equation, return True immediately
            return True
    
    return False

def calculate_equation(equation):
    result = equation[0]
    
    for i in range(1, len(equation), 2):
        operator = equation[i]
        number = equation[i + 1]
        
        if operator == '+':
            result += number
        elif operator == '*':
            result *= number
        elif operator == '||':
            # Convert both numbers to strings, concatenate, then convert back to int
            result = int(str(result) + str(number))
            
    return result

# -- #

data = readInputFile()
# data = readInputFile(test_input=True)
result = part1(data)
print(f'THE RESULT : {result}')
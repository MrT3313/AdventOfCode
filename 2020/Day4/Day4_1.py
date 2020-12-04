import re       # Python RegEx Package

def passportVerification():
    # Get Input Data
    f = open("2020/Day4/Day4_input.txt", "r")
    input = f.read()
    passports = input.split("\n\n")
    f.close()

    # Variables
    requiredFields = [ 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    validPassports = 0

    # Loop through all passports
    for _ in passports: 
        # Variables
        passportData = {}
        valid = True
        
        # Split on spaces & newlines
        passportArray = re.split('\s', _)
        
        # Add individual key value pairs to passportData object
        for _ in passportArray:
            split = _.split(':')
            passportData[split[0]] = split[1]
        
        # Check for all requires fields
        for _ in requiredFields:
            if _ not in passportData:
                valid = False
                break

        # Increment counter
        if valid == True: 
            validPassports += 1

    # RETURN
    return validPassports

# TEST
result = passportVerification()
print(result)
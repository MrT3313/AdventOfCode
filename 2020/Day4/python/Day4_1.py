import re       # Python RegEx Package

def readInputData():
    # Get Input Data
    f = open("2020/Day4/Day4_input.txt", "r")
    input = f.read()
    dataArray = input.split("\n\n")
    f.close()

    return dataArray

def getPassportObjects(array, result = []):
    for _ in array:
        # Variables
        dataObject = {}

        # Split on new lines & spaces
        pairs = re.split('\s', _)

        # Split each pair into key and value array
        for _ in pairs: 
            pair = _.split(':')

            # Add data to object
            dataObject[pair[0]] = pair[1]

        # Add object to result array
        result.append(dataObject)

    return result

def verifyFields(obj, validate = False):
    # Variables
    requiredFields = [ 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    # Check for all required fields
    for _ in requiredFields:
        if _ not in obj:
            # print('FALSE - Missing Value')
            return False
        
        if _ in obj and validate == True:
            if validateData([_, obj[_]]) == False:
                # print('FALSE', _, obj)
                return False

    return True

def validateData(data):
    if data[0] == 'byr':
        value = int(data[1])
        if value < 1920 or value > 2002:
            return False

    if data[0] == 'iyr':
        value = int(data[1])
        if value < 2010 or value > 2020:
            return False
    
    if data[0] == 'eyr':
        value = int(data[1])
        if value < 2020 or value > 2030:
            return False

    if data[0] == 'hgt':
        # Get Units
        units = data[1][-2:]
        # Check Units
        if units != 'cm' and units != 'in':
            return False
        
        # Get Value
        value = int(data[1][:-2])
        # Check Value
        if units == 'cm':
            if value < 150 or value > 193:
                return False
        
        if units == 'in':
            if value < 59 or value > 76:
                return False

    if data[0] == 'hcl':
        value = data[1]
        if value[0] != "#":
            return False
        
        if len(value[1:]) != 6:
            return False

    if data[0] == 'ecl':
        options = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        value = data[1]

        if value not in options:
            return False
    
    if data[0] == 'pid':
        try:
            int(data[1])
        except ValueError:
            return False

        if len(data[1]) != 9:
            return False

def passportVerification():
    # Variables
    validPassports = 0

    # Data
    passports = readInputData()
    arrayOfObjects = getPassportObjects(passports)

    # Loop through all passport objects
    for _ in arrayOfObjects:
        # Verify all required fields
        if verifyFields(_) == True:
            # Increment Counter
            validPassports += 1

    return validPassports

# TEST
# result = passportVerification()
# print(result)
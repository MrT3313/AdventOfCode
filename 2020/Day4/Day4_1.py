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
        # print(pairs)

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
            return False
        
        if _ in obj and validate == True:
            if validateData(_) == False:
                return False

    return True

def validateData(data):
    pass

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
result = passportVerification()
print(result)
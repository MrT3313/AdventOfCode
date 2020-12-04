from Day4_1 import readInputData, getPassportObjects, verifyFields

def verifyAndValidate():
    # Variables
    validPassports = 0

    # Data
    passports = readInputData()
    arrayOfObjects = getPassportObjects(passports)

    # Loop through all passport objects
    for _ in arrayOfObjects:
        # Verify all required fields
        if verifyFields(_, validate = True) == True:
            # Increment Counter
            validPassports += 1
    
    # RETURN
    return validPassports

# # TEST
result = verifyAndValidate()
print(result)
from functools import reduce

def readInputData():
    # Get Input Data
    f = open("2020/Day6/Day6_input.txt", "r")
    input = f.read()
    dataArray = input.split("\n\n")
    f.close()

    return dataArray

def commonQuestionsInGroup():
    # _Variables_
    data = readInputData()
    result = []

    # Get Groups
    for group in data:
        # _Variables_
        commonQuestions = set()
        invalidQuestions = set()

        # Get people
        people = group.split('\n')
        sortedPeople = sorted(people, key=len)
        # Get person w/ most answered questions
        longest = sortedPeople.pop()
        
        # Loop through longest
        for char in longest:
            # _Variables_
            valid = True

            # Check char for every person in the group
            for person in sortedPeople:
                if char not in person: 
                    invalidQuestions.add(char)
                    valid = False
                    continue
            if valid == True:
                commonQuestions.add(char)
        
        result.append([
            len(commonQuestions),
            {
                'common': commonQuestions,
                'invalid': invalidQuestions
            }
        ])

    # Get Sum
    sum = 0
    for _ in result:
        sum += _[0]
    return sum

# TEST
# result = commonQuestionsInGroup()
# print(result)    

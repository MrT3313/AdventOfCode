from functools import reduce

def readInputData():
    # Get Input Data
    f = open("2020/Day6/Day6_input.txt", "r")
    input = f.read()
    dataArray = input.split("\n\n")
    f.close()

    return dataArray

def uniqueQuestionsInGroup():
    # _Variables_
    data = readInputData()
    result = []

    # Get Groups
    for group in data:
        # _Variables_
        seenQuestions = set()

        # Get people
        people = group.split('\n')
        # Loop through people in group
        for person in people:
            # Loop through each persons answers
            for char in person:
                # Add unique characters to set()
                if char not in seenQuestions:
                    seenQuestions.add(char)

        result.append(len(seenQuestions))
    
    # Get sum of array
    sum = reduce((lambda a, b: a + b), result)
    return sum

# TEST
result = uniqueQuestionsInGroup()
print(result)
# IMPORTS
from Day3_1 import traverseMatrix
from numpy import prod

def checkManyPaths(listOfSlopes):
    # Variables
    data = []
    
    # Loop
    for _ in listOfSlopes:
        data.append(traverseMatrix(_))
    
    print(data)
    return prod(data)

# TEST
# result = checkManyPaths([
#     (1,1),
#     (3,1),
#     (5,1),
#     (7,1),
#     (1,2),
# ])
# print(result)
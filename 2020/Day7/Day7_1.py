import re

def readInputData():
    # Get Input Data
    f = open("2020/Day7/Day7_input.txt", "r")
    input = f.read()
    dataArray = input.split("\n")
    f.close()

    return dataArray

def getBagRules(str):
    '''
    Line Structure
        PART 1 = Parent
        PART 2 = Child


        Part 1: <bagColor> + 'bags' + 'contain'                                    
                    1          2          3
            - Notes: 
                1: `bagColor` can be > 1 word
                2: always plural
                3: always singular
            
            - Regex: 
                ^([a-z\s?]+) bags?

        Part 2:
                <#> + <bagColor> 'bag[s]', ... + '.'
                            1        2      3     4
            - Notes:
                1: `bagColor` can be > 1 word
                2: can be singular OR plural
                3: repeats 1 & 2 for each connected bag in line
                4: always ends the line 
            
            - Regex:
                ([0-9]+)\s+([a-z]+\s+[a-z]+)
    '''
    # Get Parent Bag
    REGEX_parent = r'^([a-z\s?]+) bags?'
    parent = re.findall(REGEX_parent, str.split('contain')[0])
    print('PARENT: ', parent)

    # Get Bag Rules
    REGEX_child = r'([0-9]+)\s+([a-z]+\s+[a-z]+)'
    children = re.findall(REGEX_child, str.split('contain')[1])
    print('CHILDREN: ', children)

    return parent, children

def canHoldTarget(target, bag, rules):
    # Edge Case
    if bag not in rules:
        return False
    
    # Check Current Bag
    if target in rules[bag]:
        # print(bag, rules[bag])
        return True

    # Check Current.Child Bags
    return any([canHoldTarget(target, child, rules) for child in rules[bag]])    

def luggageNestingDoll(target = 'shiny gold'):
    # Input
    data = readInputData()
    
    # Variables
    rules = dict()
    allBags = set()

    # Loop through each line / `rule`
    for line in data:
        # Get Data
        parent, children = getBagRules(line)
        ''' 
        parent = []
        children = [
            ('#', '<bagColor>'), ... 
        ]
        '''

        # Add Rules
        if len(children) > 0:
            rules.update(
                { parent[0]: {child[1] : child[0] for child in children} }
            )
        # Add Parent Bag
        allBags.add(parent[0])  
    
    # Loop through all bags and check if they (or their children) can hold the target
    return sum([1 if canHoldTarget(target, bag, rules) else 0 for bag in allBags])

# TEST
result = luggageNestingDoll()
print(result)
class tree:
    def __init__(self, connections = []):
        self.connections = connections
        
class node:
    def __init__(self):
        self.prev = None
        self.next = None
        

def getData():
    # Get Input Data
    f = open("2020/Day7/Day7_input.txt", "r")
    input = f.read()
    data = input.split("\n")
    f.close()

    return data 

def readLine(str):
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

    # Get Bag Rules
    REGEX_child = r'([0-9]+)\s+([a-z]+\s+[a-z]+)'
    children = re.findall(REGEX_child, str.split('contain')[1])

    return parent, children

def makeTree():

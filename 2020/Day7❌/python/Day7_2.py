# IMPORTS
from Day7_1 import getData, seedBagRules

# FUNCTIONS

# MAIN
data = getData()

# _variables_
TEST_INPUT = [
    'shiny gold bags contain 2 dark red bags.',
    'dark red bags contain 2 dark orange bags.',
    'dark orange bags contain 2 dark yellow bags.',
    'dark yellow bags contain 2 dark green bags.',
    'dark green bags contain 2 dark blue bags.',
    'dark blue bags contain 2 dark violet bags.',
    'dark violet bags contain no other bags.',
] # --> 126

# Get Bag data
# allbags, rules = seedBagRules(data)
allbags, rules = seedBagRules(TEST_INPUT)

STARTING_BAG = 'shiny gold'
total = 0


def getBagCount(color, rules, total = 0):
    for key in rules[STARTING_BAG]:
        print(key)
        print('sdfaf', rules[key])
    

#     print(rules[color])
#     print(type(rules[color]))



#     for bag in rules[color].keys():
#         total += getBagCount(bag, rules, total)

# print('INITIAL RULES: ',rules[STARTING_BAG], )



result = getBagCount(STARTING_BAG, rules)
# print(result)



exit()










# NOT MY SOLUTION: https://dev.to/qviper/advent-of-code-2020-python-solution-day-7-5319
my_bag = "shiny gold"
bags_contains = {}
# test_bags=all_bags
for k, v in rules.items():
    bags_contains[k] = []
    # print(bags_contains)
    try:
        for kk, vv in v.items():
            bags_contains[k] += [kk] * int(vv)
    except:
        pass
# c=0

print(bags_contains)

def count_bags(current_bag):
    if current_bag == " " or bags_contains.get(current_bag) is None:
        return 0

    #print("key:", current_bag)
    cnt = len(bags_contains[current_bag])
    cnts = []
    for k in bags_contains[current_bag]:
        cnts.append(count_bags(k))    
    return sum(cnts)+cnt

print(f"{my_bag} bag can hold {count_bags(my_bag)} bags")
























# STARTING_BAG = 'shiny gold'

# # Get Data
# # allbags, rules = seedBagRules(data)
# allbags, rules = seedBagRules(TEST_INPUT)
# # print(allbags)
# print('Rules', rules)

# STARTING_RULES = rules[STARTING_BAG]
# print('Starting Bag Rule(s)',STARTING_RULES)
# print('type',type(STARTING_RULES))

# # print(rules[STARTING_BAG])
# # print(type(rules[STARTING_BAG]))
# # print(len(rules[STARTING_BAG]))

# total = 0

# # Add initial bags
# total += len(STARTING_RULES)
# print('TOTAL', total)



# # for child in STARTING_RULES.items():
# #     print('CHILD',child)
# #     total += child[1] * getBagCount(child[0], rules)




#     # subChildren = child.items()
#     # print('SUB CHILDREN: ', subChildren)


# #     # _variables_
# #     paths[level] 
    

# #     print(child)

# #     print(rules[child[0]])




# # for child in rules[STARTING_BAG]:
# #     multiplier 
# #     print(child)
# #     exit()
# #     if count == 0: 
# #         count = 1

# #     print('CHILD: ', child)
# #     print('New Rules',rules[child])

# #     count = count * rules[child]




# # --RESULT--

import pprint
from typing import Dict, Set

def readInputFile(test_input=False):
    if test_input:
        f = open("../test_input.txt", "r")
    else:
        f = open("../input.txt", "r")

    data = f.read()
    split = data.split('\n\n')

    rules = split[0].splitlines()
    updates = split[1].splitlines()

    f.close()

    return rules, updates

class Node:
    def __init__(self, id: int, prerequisites: list = None):
        self.id = id
        self.prerequisites = prerequisites if prerequisites else []

    def __repr__(self):
        return f"Node(id={self.id}, prerequisites={[p.id for p in self.prerequisites]})"
    
    def __hash__(self):
        return hash(self.id)
    
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.id == other.id
        return False

class Graph:
    def __init__(self):
        self.nodes: Dict[int, Set[Node]] = {}
    
    def size(self):
        return len(self.nodes)
    
    def get_node(self, node_id: int) -> Node:
        for node in self.nodes.keys():
            if node.id == node_id:
                return node
        return None
    
    def add_node(self, node_id: int) -> Node:
        existing_node = self.get_node(node_id)
        if existing_node:
            return existing_node
            
        new_node = Node(id=node_id)
        self.nodes[new_node] = set()
        return new_node
    
    def add_edge(self, parent_id: int, child_id: int):
        parent_node = self.add_node(parent_id)
        child_node = self.add_node(child_id)
        
        # Add edge
        self.nodes[parent_node].add(child_node)
        
        # Update prerequisites
        if parent_node not in child_node.prerequisites:
            child_node.prerequisites.append(parent_node)
    
    def visualize(self):
        print("\nGraph Visualization:")
        print("-------------------")
        for node, children in self.nodes.items():
            print(f"\nNode {node.id}:")
            print(f"  Prerequisites: {[p.id for p in node.prerequisites]}")
            print(f"  Children: {[child.id for child in children]}")

def part1(rules, updates):
    graph = Graph()
    
    #################
    # PROCESS RULES #
    #################
    print("\n...Processing Rules...")
    for rule in rules:
        parent, child = map(int, rule.split('|'))
        graph.add_edge(parent, child)
    
    # Process updates
    print("\n...Processing Updates...")
    valid = []
    invalid = []

    for update in updates:
        nodes = [int(x) for x in reversed(update.split(','))]
        print(f"\nChecking nodes: {nodes}")
        update_valid = True

        nodes_copy = nodes
        for i, node_id in enumerate(nodes_copy):
            node = graph.get_node(node_id)
            if node:
                print(f"Found node {node_id} with prerequisites: {[p.id for p in node.prerequisites]}")

                if i < len(nodes_copy) - 1:
                    prev_node_id = nodes[i + 1]  # Get the previous node in sequence
                    # Check if the previous node is in prerequisites
                    prev_node = graph.get_node(prev_node_id)
                    if prev_node not in node.prerequisites:
                        print(f"Invalid: Node {node_id} doesn't have {prev_node_id} as a prerequisite")
                        update_valid = False
                        break
                    else: 
                        update_valid = True
                        print(f'Valid: update {nodes}')
            

            else:
                print(f"Node {node_id} not found in graph")
        
        if update_valid:
            valid.append(update)
        else:
            invalid.append(update)

    # CALCULATE: part1_answer
    part1_answer = sum(
        int(update.split(',')[len(update.split(','))//2]) for update in valid
    )
    print(f"\n\n🎉🎉🎉🎉PART 1 ANSWER : {part1_answer} 🎉🎉🎉🎉\n\n")

    part2_answer = part2(graph, invalid)
    
    return graph

def part2(graph, invalid):
    '''
    Reorders invalid updates according to the graph rules.
    Returns the sum of middle elements from the correctly ordered sequences.
    '''
    corrected_updates = []

    for update in invalid:
        nodes = [int(x) for x in update.split(',')]
        ordered_nodes = []
        remaining_nodes = set(nodes)

        # Keep adding nodes until we've used them all
        while remaining_nodes:
            # Find a node that has no prerequisites in the remaining set
            for node_id in remaining_nodes:
                node = graph.get_node(node_id)
                prereq_ids = {p.id for p in node.prerequisites}
                # If all prerequisites are either satisfied or not in our remaining set
                if not (prereq_ids & remaining_nodes):
                    ordered_nodes.append(node_id)
                    remaining_nodes.remove(node_id)
                    break

        corrected_update = ','.join(map(str, ordered_nodes))
        corrected_updates.append(corrected_update)
        # print(f"{update} becomes {corrected_update}")

    # Calculate part 2 answer similar to part 1
    part2_answer = sum(
        int(update.split(',')[len(update.split(','))//2]) for update in corrected_updates
    )
    print(f"\n\n🎉🎉🎉🎉PART 2 ANSWER : {part2_answer} 🎉🎉🎉🎉\n\n")
    
    return part2_answer


# ---- #

rules, updates = readInputFile()
# rules, updates = readInputFile(test_input=True)
result = part1(rules, updates)
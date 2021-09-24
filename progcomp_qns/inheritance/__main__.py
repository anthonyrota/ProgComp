import sys


class Node:
    def __init__(self):
        self.name = None
        self.parent = None
        self.deceased = False
        self.gender = None
        self.children = []

    def __str__(self):
        return str([self.name, '' if not self.parent else self.parent.name, [child.name for child in self.children]])


nodes = {}
start_node = None

num_lines = int(sys.stdin.readline())
for i in range(num_lines):
    line = sys.stdin.readline().strip()
    parent, children = line.split(':')
    parent_node_name = parent.strip('x*')
    if parent_node_name in nodes:
        parent_node = nodes[parent_node_name]
    else:
        parent_node = Node()
        parent_node.name = parent_node_name
        parent_node.gender = parent_node_name[0]
        nodes[parent_node_name] = parent_node
    if parent[-1] == 'x':
        parent_node.deceased = True
    elif parent[-1] == '*':
        start_node = parent_node
    children = children.strip()
    if children == '':
        continue
    children = children.split(' ')
    for child_name in children:
        if child_name in nodes:
            child_node = nodes[child_name]
        else:
            child_node = Node()
            child_node.name = child_name
            child_node.gender = child_name[0]
            nodes[child_name] = child_node
        child_node.parent = parent_node
        parent_node.children.append(child_node)

male_order = []
female_order = []

# Females don't have descendants?


def visit(node, exclude_child=None):
    for child in node.children:
        if child == exclude_child:
            continue
        if child.gender == 'M':
            if not child.deceased:
                male_order.append(child)
        visit(child)
    female_children = []
    for child in node.children:
        if child.gender == 'F':
            if not child.deceased:
                female_children.append(child)
    if female_children:
        female_order.append(female_children)


visit(start_node)
prev_node = start_node
while prev_node.parent:
    visit(prev_node.parent, prev_node)
    prev_node = prev_node.parent

order = [start_node.name]
for male in male_order:
    order.append(male.name)
for female_group in female_order:
    order.append('+'.join(female.name for female in female_group))

print(' '.join(order))

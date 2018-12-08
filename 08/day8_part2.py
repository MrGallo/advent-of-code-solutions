from collections import namedtuple


Node = namedtuple('Node', 'children metadata value')
# tree_data = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2".split()
tree_data = open('input.txt').read().split()


def parse_tree_data(start):
    global tree_data
    num_children = int(tree_data[start])
    num_metadata = int(tree_data[start+1])
    children = []

    # append children
    for _ in range(num_children):
        child = parse_tree_data(start + 2)
        children.append(child)

    meta_start = start + 2
    meta_end = meta_start + num_metadata
    metadata = [int(n) for n in tree_data[meta_start:meta_end]]
    tree_data = tree_data[:start] + tree_data[meta_end:]

    if not children:
        value = sum(metadata)
    else:
        value = 0
        for child_num in metadata:
            try:
                value += children[child_num - 1].value
            except IndexError:
                pass

    return Node(children=children, metadata=metadata, value=value)


root = parse_tree_data(0)
print(root.value)

DIRECTION_MAP = dict(zip("LR", (0, 1)))


def main():
    with open("input.txt", "r") as f:
        lines = f.read().split("\n")

    steps = lines[0]

    nodes = {}
    for line in lines[2:]:
        node_name, children_str = line.split(" = ")
        children_str = children_str[1:-1]
        children = tuple(children_str.split(", "))
        nodes[node_name] = children

    

    # result = part_one(steps, nodes)
    # print(result)  # 17287

    result = part_two(steps, nodes)
    print(result)


def part_one(steps, nodes):
    position = "AAA"
    steps_required = 0
    for step in iterate_steps(steps):
        # print(position)
        # input()
        if position == "ZZZ":
            break
        index = DIRECTION_MAP[step]
        next_node_name = nodes[position][index]
        position = next_node_name
        steps_required += 1
    return steps_required


def part_two(steps, nodes):
    positions = []
    for name in nodes.keys():
        if name[-1] == "A":
            positions.append(name)
    
    steps_required = 0
    for step in iterate_steps(steps):
        count_z = len(positions)
        for i, position in enumerate(positions):
            index = DIRECTION_MAP[step]
            next_node_name = nodes[position][index]
            if next_node_name[-1] != "Z":
                count_z -= 1
            positions[i] = next_node_name
        
        steps_required += 1

        if count_z == len(positions):
            break
    
    return steps_required


def all_positions_end_with_z(positions):
    all_z = True
    count = len(positions)
    for position in positions:
        if position[-1] != "Z":
            all_z = False
            count -= 1
    
    return all_z

def iterate_steps(steps: str):
    i = 0
    while True:
        yield steps[i % len(steps)]
        i += 1

if __name__ == "__main__":
    main()
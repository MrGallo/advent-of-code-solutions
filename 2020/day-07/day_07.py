import re


def main():
    with open('input.txt', 'r') as f:
        lines = f.read().split("\n")
    
    color_rules = {}
    for line in lines:
        color, contents_str = line.split(" bags contain ")

        matches = re.finditer(r"([0-9]+) (.+?) bag", contents_str)
        rules = []
        for match in matches:
            rules.append((int(match.group(1)), match.group(2)))
        color_rules[color] = rules
        

    count = 0
    for color, rule in color_rules.items():
        path = find_path(color, color_rules)
        if "shiny gold" in path:
            count += 1
    print(count)  # Part 1: 265


    print(find_num_contents("shiny gold", color_rules))  # Part 2: 14177


def find_path(current_node, color_rules):
    contents = []
    for _, child in color_rules[current_node]:
        contents += [child] + find_path(child, color_rules)
    return contents


def find_num_contents(current_node, color_rules):
    total = 0
    for number, child in color_rules[current_node]:
        total += number * (1 + find_num_contents(child, color_rules))
    return total


def tests():
    assert find_path("a", {"a": [(1, "b")], "b": []}) == ['b']
    assert find_path("a", {"a": [(2, "b"), (1, "c")], "b": [], "c": [(3, "b")]}) == ['b', 'c', 'b']

    assert find_num_contents("a", {"a": [(1, "b")], "b": []}) == 1
    assert find_num_contents("a", {"a": [(2, "b")], "b": []}) == 2
    assert find_num_contents("a", {"a": [(2, "b"), (1, "c")], "b": [], "c": [(3, "b")]}) == 6


if __name__ == "__main__":
    tests()
    main()
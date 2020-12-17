import re
from typing import List


def main():
    with open('input.txt', 'r') as f:
        source = f.read().split("\n")
    

    print(part_1(source))  # Part 1: 17481577045893
    print(part_2(source))  # Part 2: 4160009892257


def part_1(source):
    mem = {}
    mask = None
    for line in source:
        regex = r'mask = (.+)'
        match = re.match(regex, line)
        if match:
            mask = match.group(1)
        else:
            regex = r'mem\[([0-9]+)\] = ([0-9]+)'
            match = re.match(regex, line)
            loc = int(match.group(1))
            value = int(match.group(2))

            value_binary_str = str(bin(value))[2:].zfill(36)
            
            value_to_write_str = ""
            for m, v in zip(mask, value_binary_str):
                if m == 'X':
                    value_to_write_str += v
                else:
                    value_to_write_str += m
            value_to_write = int(value_to_write_str, base=2)
            mem[loc] = value_to_write

    return sum(mem.values())
    
def part_2(source):
    mem = {}
    mask = None
    for line in source:
        regex = r'mask = (.+)'
        match = re.match(regex, line)
        if match:
            mask = match.group(1)
        else:
            regex = r'mem\[([0-9]+)\] = ([0-9]+)'
            match = re.match(regex, line)
            loc = int(match.group(1))
            value = int(match.group(2))

            floating = decode_memory_location(loc, mask)
            locations = [int(loc) for loc in all_floating(floating)]
            for location in locations:
                mem[location] = value

    return sum(mem.values())


def decode_memory_location(location: int, mask: str) -> str:
    loc_str = str(bin(location))[2:].zfill(36)

    mem_loc_str = ""
    for m, v in zip(mask, loc_str):
        if m == "0":
            mem_loc_str += v
        else:
            mem_loc_str += m
    return mem_loc_str


def all_floating(floating_address: str) -> List[str]:
    def merge(char, children):
        return [char + child for child in children] if children else [char]

    if floating_address == "":
        return []
    
    floating = []
    children = all_floating(floating_address[1:])
    if floating_address[0] == "X":
        floating = merge("0", children) + merge("1", children)
    else:
        floating = merge(floating_address[0], children)
    
    return floating


def tests():
    mask = "000000000000000000000000000000X1001X"
    assert decode_memory_location(42, mask) == "000000000000000000000000000000X1101X"

    expected = [
        "000000000000000000000000000000011010",
        "000000000000000000000000000000011011",
        "000000000000000000000000000000111010",
        "000000000000000000000000000000111011"
    ]
    assert all_floating("000000000000000000000000000000X1101X") == expected
    assert len(all_floating("X" * 10)) == 2**10

    assert len(all_floating("X0X")) == 4


if __name__ == "__main__":
    tests()
    main()
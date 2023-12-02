def determine_marker_start(string: str, length: int = 4) -> int:
    for i in range(len(string) - length):
        substr = string[i:i + length]
        check = set(substr)
        if len(check) == length:
            return i + length


# test only
# test_lines = []
# with open("test.txt", "r") as f:
#     test_lines = f.read().split("\n")
# print(test_lines)
# for line in test_lines:
#     print(determine_marker_start(line))


with open("input.txt", "r") as f:
    data = f.read().strip()

print(determine_marker_start(data))             # part 1: 1093
print(determine_marker_start(data, length=14))  # part 2: 3534

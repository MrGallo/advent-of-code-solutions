
def main():
    report = []
    with open("input.txt", "r") as f:
        for line in f.read().split("\n"):
            record, group_nums = line.split(" ")
            group_nums = list(map(int, group_nums.split(",")))
            report.append((record, group_nums))

    print(part1(report))  # Part 1: 7490
    print(part2(report))  # Part 2: 65607131946466


def part1(report):
    count = 0
    for record, groupings in report:
        count += possibilities(record, groupings)

    return count


def part2(report):
    unfolded = []
    for record, groupings in report:
        unfolded_record = "?".join([record] * 5)
        unfolded_groupings = groupings * 5
        unfolded.append((unfolded_record, unfolded_groupings))

    count = 0
    for record, groupings in unfolded:
        count += possibilities(record, groupings)

    return count


def possibilities(record, groupings, index = 0, memo = None):
    if memo is None:
        memo = {}
    
    if index == len(groupings):
        if "#" not in record:
            return 1
        else:
            return 0

    group_size = groupings[index]
    if group_size > len(record):
        return 0
    
    group = record[:group_size].replace("?", "#")
    try:
        after = record[group_size]
    except IndexError:  # end of record
        after = ""

    try:
        return memo[(record, tuple(groupings), index)]
    except KeyError:
        pass # not in memo, do the work

    count = 0
    if group == "#" * group_size and after != "#":  # include it
        count += possibilities(record[group_size + 1:], groupings, index + 1, memo)
    
    if record[0] != "#":
        count += possibilities(record[1:], groupings, index, memo)

    memo[(record, tuple(groupings), index)] = count

    return count


if __name__ == "__main__":
    main()
def look_and_sayify(original):
    orig_list = [int(n) for n in original]

    new_string = ""
    n = 0
    current = orig_list[0]
    next = None

    i = 0
    while i < len(orig_list):
        while not next or current == next:
            n += 1
            i += 1

            try:
                next = orig_list[i]
            except IndexError:
                next = orig_list[-1]
                break

        new_string += f"{n}{current}"
        current = next
        n = 0

    return new_string


problem_input = "1113122113"

for _ in range(50):
    problem_input = look_and_sayify(problem_input)

print(len(problem_input))  # answer part 1: 360154
                           # answer part 2: 5103798

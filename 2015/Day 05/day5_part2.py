def has_repeated_pair(string):
    for i in range(0, len(string) - 1):
        needle = string[i:i + 2]
        for j in range(i + 2, len(string) - 1):
            if string[j:j + 2] == needle:
                return True
    return False


def has_aba_pattern(string):
    for i in range(len(string) - 2):
        a, b, c, = string[i:i + 3]
        if a == c:
            return True
    return False


with open('input.txt') as f:
    potential_strings = [s.strip() for s in f]

nice_strings = []
for potential_string in potential_strings:
    if has_repeated_pair(potential_string) and has_aba_pattern(potential_string):
        nice_strings.append(potential_string)

print(len(nice_strings))  # answer: 55

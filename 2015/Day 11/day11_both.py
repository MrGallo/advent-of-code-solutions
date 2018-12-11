def find_next_valid_password(string):
    while True:
        string = increment_string(string)
        if password_valid(string):
            return string


def password_valid(string):
    return has_increasing_straight(string) and lacks_oil(string) and has_two_diff_pairs(string)


def has_increasing_straight(string):
    for i in range(len(string)-3):
        current_three = string[i:i+3]
        actual_ords = [ord(c) for c in current_three]
        first_ord = ord(current_three[0])
        expected_ords = [n for n in range(first_ord, first_ord+3)]

        if actual_ords == expected_ords:
            return True

    return False


def lacks_oil(string):
    for char in string:
        if char in "oil":
            return False
    return True


def has_two_diff_pairs(string):
    first_match = None
    i = 0
    while i < len(string)-1:
        char = string[i]
        next_char = string[i+1]

        if char == next_char:
            if not first_match:
                first_match = char
            elif char != first_match:
                return True
        i += 1

    return False


def increment_string(string):
    ord_list = [ord(c) for c in string]

    new_string = ""
    increment = True
    i = len(string)-1
    while increment and i >= 0:
        if ord_list[i] != ord('z'):
            increment = False
        new_string = chr((ord_list[i] - 97 + 1) % 26 + 97) + new_string
        i -= 1

    return string[:i+1] + new_string


problem_input = "vzbxkghb"

new_password = find_next_valid_password(problem_input)  # answer part 1: vzbxxyzz
print(new_password)

new_password = find_next_valid_password(new_password)   # answer part 2: vzcaabcc
print(new_password)


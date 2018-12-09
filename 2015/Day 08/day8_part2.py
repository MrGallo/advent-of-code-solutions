with open('input.txt') as f:
    strings = [line.strip() for line in f]

new_code_characters = 0
code_characters = 0

for string in strings:
    new_code_string = "\""
    for char in string:
        if char in "\"\\":
            new_code_string += "\\" + char
        else:
            new_code_string += char
    new_code_string += "\""

    code_characters += len(string)
    new_code_characters += len(new_code_string)

print(new_code_characters - code_characters)

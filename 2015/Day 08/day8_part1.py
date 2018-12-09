with open('input.txt') as f:
    strings = [line.strip() for line in f]

code_characters = 0
word_characters = 0

for string in strings:
    code_characters += 2  # each line enclosed with quotes
    i = 1
    while i < len(string)-1:

        char = string[i]
        advance = 0
        if char == "\\":
            next_char = string[i+1]
            if next_char == "x":
                advance = 3
            else:
                advance = 1

        word_characters += 1
        code_characters += 1 + advance
        i += 1 + advance

print(code_characters - word_characters)  # answer: 1342

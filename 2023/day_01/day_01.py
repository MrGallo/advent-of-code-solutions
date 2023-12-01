"""
Overkill recursive functions to get the left-most number and then another
function to get the right-most number.

Better solution: day_01_simpler.py
"""

words = "one two three four five six seven eight nine"
WORD_NUMBERS = list(zip(words.split(), range(1, len(words) + 1)))

def get_left(line: str, include_words=False) -> int:
    if len(line) == 0:
        return 0

    first = line[0]
    if first.isdigit():
        return int(first)
    
    if include_words:
        for word, number in WORD_NUMBERS:
            if line.startswith(word):
                return number
    
    return get_left(line[1:], include_words)

def get_right(line: str, include_words=False) -> int:
    if len(line) == 0:
        return 0
    
    last = line[-1]
    if last.isdigit():
        return int(last)
    
    if include_words:
        for word, number in WORD_NUMBERS:
            if line.endswith(word):
                return number
        
    return get_right(line[:len(line) - 1], include_words)

lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()

# PART 1
values = []
for line in lines:
    line = line.strip()
    first = get_left(line)
    last = get_right(line)
    value = 10 * first + last
    values.append(value)

print(sum(values))  # part 1: 55108

# PART 2
values = []
for line in lines:
    line = line.strip()
    first = get_left(line, include_words=True)
    last = get_right(line, include_words=True)
    value = 10 * first + last
    values.append(value)

print(sum(values))  # part 2: 56324
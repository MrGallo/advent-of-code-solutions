"""
"Just loop through to find the numbers then take the first and last."
Credit: Olivia

Me: 🤦
"""

lines = []
with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

# PART 1
total = 0
for line in lines:
    nums = []
    for c in line:
        if c.isdigit():
            nums.append(int(c))
    first = nums[0]
    last = nums[-1]
    total += first * 10 + last

print(total)  # 55108

# PART 2
words = "one two three four five six seven eight nine"
word_nums = list(zip(words.split(), range(1, len(words))))

total = 0
for line in lines:
    nums = []
    for i in range(len(line)):
        c = line[i]
        if c.isdigit():
            nums.append(int(c))
            continue

        for word, number in word_nums:
            if line[i:].startswith(word):
                nums.append(number)
                break
        
    first = nums[0]
    last = nums[-1]
    total += first * 10 + last

print(total)  # 56324
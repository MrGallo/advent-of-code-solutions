from collections import Counter

with open('input.txt') as f:
    inputs = [int(n) for n in f]

current_frequency = 0
frequency_counts = Counter()
frequency_counts[current_frequency] += 1

i = 0
while True:
    change = inputs[i % len(inputs)]
    current_frequency += change
    frequency_counts[current_frequency] += 1
    if frequency_counts[current_frequency] == 2:
        duplicate_found = True
        break
    i += 1

print(current_frequency)

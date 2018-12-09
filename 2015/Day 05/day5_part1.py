with open('input.txt') as f:
    strings = [s.strip() for s in f]

nice_strings = []

forbidden_strings = ['ab', 'cd', 'pq', 'xy']
for potential_string in strings:
    forbidden = False

    for forbidden_string in forbidden_strings:
        if forbidden_string in potential_string:
            forbidden = True
            break

    i = 0
    vowel_count = 0
    repeated_letter = False
    while i < len(potential_string):
        char = potential_string[i]

        if char in 'aeiou':
            vowel_count += 1

        # at least one letter shows twice in a row
        if i < len(potential_string) - 1 and char == potential_string[i + 1]:
            repeated_letter = True
        i += 1

    enough_vowels = vowel_count >= 3

    if enough_vowels and (not forbidden) and repeated_letter:
        nice_strings.append(potential_string)

print(len(nice_strings))  # answer: 255

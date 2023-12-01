
with open('input.txt', "r") as f:
    lines = f.readlines()

all_elf_calories = []
calories = 0
for line in lines:
    try:
        calories += int(line)
    except ValueError:
        all_elf_calories.append(calories)
        calories = 0

print(max(all_elf_calories))  # part 1: 71934
print(sum(sorted(all_elf_calories, reverse=True)[0:3]))  # part 2: 211447


schematic = []

with open("input.txt", "r") as f:
    for line in f.readlines():
        schematic.append(line.strip())

    
# print(schematic)
numbers = []
symbol_adjacent = set()
for row_i in range(len(schematic)):
    # print(schematic[row_i])
    writing = False
    number_chars = ""
    number_cells = []
    for col_i in range(len(schematic[row_i])):
        c = schematic[row_i][col_i]
        if c.isdigit():
            writing = True
            number_chars += c
            number_cells.append((row_i, col_i))
        
        if not c.isdigit() or col_i == len(schematic[row_i]) - 1:
            if writing:
                writing = False
                # print(number_chars)
                # print(number_cells)
                numbers.append((int(number_chars), number_cells))
                number_chars = ""
                number_cells = []
            
            if not c.isdigit() and c != ".":  # its a symbol
                # print(c)
                for i in range(row_i - 1, row_i + 2):  # row
                    for j in range(col_i - 1, col_i + 2):  # column
                        symbol_adjacent.add((i, j))
                        # print(i, j)

# print(numbers)
# print(symbol_adjacent)

part_numbers = []
for number, cells in numbers:
    is_part = False
    # print(number)
    for cell in cells:
        # print(cell)
        if cell in symbol_adjacent:
            is_part = True
    if is_part:
        # print("Is part")
        part_numbers.append(number)

# print(part_numbers)
print(sum(part_numbers))  # Part 1: 514969


# PART 2

print(schematic)
numbers = []
star_positions = []
for row_i in range(len(schematic)):
    number_adjacent = []
    chars = ""
    write = False
    for col_i in range(len(schematic[0])):
        c = schematic[row_i][col_i]
        
        if c.isdigit():
            write = True
            chars += c

        is_last_char = col_i == len(schematic[row_i]) - 1
        if not c.isdigit() or is_last_char:
            if write:
                offset = 1 if not is_last_char or not c.isdigit() else 0
                for i in range(row_i - 1, row_i + 2):
                    for j in range(col_i - len(chars) - offset, col_i + 2 - offset):
                        number_adjacent.append((i, j))
                numbers.append((int(chars), number_adjacent))
            chars = ""
            number_adjacent = []
            write = False


        if c == "*":
            star_positions.append((row_i, col_i))

print(numbers)
print(star_positions)

ratio_sum = 0
ratios = []
for star_pos in star_positions:
    # print("*" * 5, star_pos)
    count = 0
    ratio = 1
    for num, adjacent_cells in numbers:
        # print(num, adjacent_cells)
        for cell in adjacent_cells:
            if cell == star_pos:
                # print(cell)
                count += 1
                ratio *= num
    if count == 2:
        ratios.append(ratio)

print(sum(ratios))
race_records = []
str_nums = []
with open("input.txt", "r") as f:
    for line in f.read().split("\n"):
        _, nums = line.split(":")
        str_nums.append(tuple(map(int, (num.strip() for num in nums.split(" ") if num))))
    for time, distance in zip(*list(str_nums)):
        race_records.append((time, distance))


count_product = 1
for time, record_distance in race_records:
    avg_speed = record_distance/time
    # print(f"Time: {time}, Record distance: {record_distance}, Avg speed:{avg_speed}" + "*" * 10)
    count = 0
    for time_held in range(time + 1):
        time_remaining = time - time_held
        distance = time_held * time_remaining
        if distance > record_distance:
            count += 1
        # print(f"{time_held = }, {time_remaining = }, {distance = }")
    count_product *= count

print(count_product)  # Part 1: 741000

# PART 2
print(race_records)

# fix kerning issue
top_line = ""
bottom_line = ""
for t, d in race_records:
    top_line += str(t)
    bottom_line += str(d)

time = int(top_line)
record_distance = int(bottom_line)

count = 0
for time_held in range(time + 1):
    time_remaining = time - time_held
    distance = time_held * time_remaining
    if distance > record_distance:
        count += 1
    # print(f"{time_held = }, {time_remaining = }, {distance = }")

print(count)  # Part 2:
    
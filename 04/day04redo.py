# inspired by: https://www.reddit.com/r/adventofcode/comments/a2xef8/2018_day_4_solutions/eb1wb5a
from collections import defaultdict

with open('input.txt') as f:
    lines = sorted([line.strip() for line in f.readlines()])

guards_total_mins = defaultdict(int)
guards_specific_minutes = defaultdict(int)


for line in lines:
    if "#" in line:
        id_i = line.index("#")
        end_i = line.index(" ", id_i)
        guard_id = int(line[id_i+1:end_i])
    elif "asleep" in line:
        minute = int(line[15:17])
        sleep_start = minute
    elif "up" in line:
        end = int(line[15:17])
        time = sleep_start
        while time < end:
            guards_total_mins[guard_id] += 1
            guards_specific_minutes[(guard_id, time)] += 1
            time += 1


best = None
for (guard_id, minute), value in guards_specific_minutes.items():
    if not best or guards_specific_minutes[best] < value:
        best = (guard_id, minute)
        print(f"key: {best}, val: {guards_specific_minutes[best]}")

g, m = best
print(g*m)
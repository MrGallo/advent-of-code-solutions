from collections import Counter

guard_sums = Counter()
guard_minutes = Counter()

with open('input.txt') as f:
    logs = sorted([line.strip() for line in f])

current_guard = None
sleep_start = None
for log in logs:
    minute = int(log[15:17])

    if "begins shift" in log:
        id_start = log.index("#") + 1
        id_end = log.index(" ", id_start)
        current_guard = int(log[id_start:id_end])
    elif "falls asleep" in log:
        sleep_start = minute
    elif "wakes up" in log:
        time = sleep_start
        while time < minute:
            guard_sums[current_guard] += 1
            guard_minutes[(current_guard, time)] += 1
            time += 1


guard_slept_most = guard_sums.most_common(1)[0][0]

best = None
for (guard, minute), times in guard_minutes.items():
    if guard == guard_slept_most:
        if not best or times > guard_minutes[best]:
            best = (guard, minute)

g, m = best
print(g*m)

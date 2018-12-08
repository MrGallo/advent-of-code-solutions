from collections import defaultdict
import string

lines = open('input.txt').read().split('\n')
# lines = """Step C must be finished before step A can begin.
# Step C must be finished before step F can begin.
# Step A must be finished before step B can begin.
# Step A must be finished before step D can begin.
# Step B must be finished before step E can begin.
# Step D must be finished before step E can begin.
# Step F must be finished before step E can begin.""".split('\n')

forward = defaultdict(list)
backward = defaultdict(list)

for line in lines:
    prereq = line[5]
    dependant = line[36]

    backward[dependant] += prereq
    forward[prereq] += dependant

start_nodes = set(forward.keys()) - set(backward.keys())

stack = sorted(list(start_nodes), reverse=True)
order = ""
cursor = -1
time = 0
in_progress = {}

print(stack)
while stack or in_progress:
    # Assign workers
    cursor = len(stack) - 1

    while len(in_progress) <= 4 and cursor >= -len(stack):
        # find next task, and assign to a worker
        next = stack.pop(cursor)
        last_prereqs = backward[next]
        can_start = True
        for prereq in last_prereqs:
            if prereq in stack or prereq in in_progress.keys():
                # cannot start progress, move along
                can_start = False
                stack.insert(cursor, next)
                break

        if can_start:
            # when all prereqs are not in stack or in progress
            time_mapping = dict(zip(string.ascii_uppercase, range(60 + 1, 60 + 27)))
            in_progress[next] = time_mapping[next]

        cursor -= 1

    # Free up workers
    remove = []
    for task, time_remaining in in_progress.items():
        in_progress[task] -= 1
        if in_progress[task] <= 0:
            remove.append(task)

    for task in remove:
        print(f'popping {task}')
        del in_progress[task]

        order += task
        current_dependants = forward[task]
        for depn in current_dependants:
            if depn not in order and depn not in stack and depn not in in_progress.keys():
                stack.append(depn)

    stack.sort(reverse=True)

    time += 1

print(time)

# HPDTNXYLOCGEQSIMABZKRUWVFJ - correct
# HPDTNXYLOCGEQSIMABZKRUWVFJ

# HPXYBDUGQLOETCNSWIMZAJFKRV - incorrect
# HPXYBDUGLOTCNQSEMIAZKRWVFJ - incorrect
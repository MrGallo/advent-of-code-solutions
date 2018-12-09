

def reaction(u1, u2):
    return u1 != u2 and u1.lower() == u2.lower()


with open('input.txt') as f:
    polymer = f.read().strip()

stack = ['.']
for unit in polymer:
    current = stack.pop()
    if not reaction(current, unit):
        stack.append(current)
        stack.append(unit)

print(len(stack)-1)

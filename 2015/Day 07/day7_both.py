memo = {}


def memoize(connection):
    try:
        return memo[connection]
    except KeyError:
        func_name, args = connection
        result = OPERATIONS[func_name](*args)
        memo[connection] = result
        return result


def follow(source):
    if type(source) is int:
        return source

    result = memoize(connections[source])
    return result


def bitwise_not(source):
    if type(source) is int:
        return ~source

    result = memoize(connections[source])
    return ~result


def bitwise_rshift(source, bits):
    if type(source) is int:
        return source >> bits

    result = memoize(connections[source])
    return result >> bits


def bitwise_lshift(source, bits):
    if type(source) is int:
        return source << bits

    result = memoize(connections[source])
    return result << bits


def bitwise_and(source1, source2):
    if type(source1) is int:
        result1 = source1
    else:
        result1 = memoize(connections[source1])

    if type(source2) is int:
        result2 = source2
    else:
        result2 = memoize(connections[source2])

    return result1 & result2


def bitwise_or(source1, source2):
    if type(source1) is int:
        result1 = source1
    else:
        result1 = memoize(connections[source1])

    if type(source2) is int:
        result2 = source2
    else:
        result2 = memoize(connections[source2])

    return result1 | result2


OPERATIONS = {
    'follow': follow,
    'NOT': bitwise_not,
    'RSHIFT': bitwise_rshift,
    'LSHIFT': bitwise_lshift,
    'AND': bitwise_and,
    'OR': bitwise_or,
}


def parse_gate(gate_string):
    components = gate_string.split()

    if len(components) == 1:
        # follow wire
        try:
            wire = int(components[0])
        except ValueError:
            wire = components[0]
        return "follow", (wire,)

    elif components[0] == "NOT":
        gate, wire = components
        try:
            wire = int(wire)
        except ValueError:
            pass
        return gate, (wire,)

    elif components[1] == "RSHIFT" or components[1] == "LSHIFT":
        wire, gate, bits = components
        try:
            wire = int(wire)
        except ValueError:
            pass
        return gate, (wire, int(bits))

    elif components[1] == "AND" or components[1] == "OR":
        wire_x, gate, wire_y = components
        try:
            wire_x = int(wire_x)
        except ValueError:
            pass

        try:
            wire_y = int(wire_y)
        except ValueError:
            pass

        return gate, (wire_x, wire_y)


lines = open('input.txt').read().split('\n')


connections = {}
for line in lines:
    arrow_index = line.index("->")
    wire_name = line[arrow_index + 3:]
    gate_string = line[:arrow_index -1]
    connections[wire_name] = parse_gate(gate_string)


# part 2 (remove for just part 1)
func_name, args = connections['b']
connections['b'] = (func_name, (46065,))
# end part 2


print(follow('a'))  # answer part 1: 46065
                    # answer part 2: 14134


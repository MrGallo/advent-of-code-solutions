
with open("input.txt", "r") as f:
    program = [int(n) for n in f.read().split(",")]


program[1] = 12
program[2] = 2

i = 0
while program[i] != 99:
    opcode, input_position1, input_position2, output_position = program[i:i+4]
    value1 = program[input_position1]
    value2 = program[input_position2]

    if opcode == 1:  # addition
        result = value1 + value2
        program[output_position] = result
    elif opcode == 2:  # multiplication
        result = value1 * value2
        program[output_position] = result
    else:
        raise Exception("Invalid op code")
    
    i += 4

print(program[0])  # answer: 3654868
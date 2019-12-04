from typing import List


def execute_program(initial_program: List[int], noun: int, verb: int) -> int:
    program = initial_program[:]  # copy initial program
    program[1] = noun
    program[2] = verb

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
            raise Exception("Invalid opcode")
        
        i += 4

    return program[0]


with open("input.txt", "r") as f:
    program = [int(n) for n in f.read().split(",")]

for noun, verb in ((n, v) for n in range(0, 100) for v in range(0, 100)):
    result = execute_program(program, noun, verb)
    if result == 19690720:
        break

print(100 * noun + verb)  # answer: 7014

from typing import Dict, List, Tuple, Union


class IntcodeComputer:
    HALT = "HALT"
    RETURNING_OUTPUT = "RETURNING_OUTPUT"
    AWAITING_INPUT = "AWAITING_INPUT"

    def __init__(self, program: List[int] = None, inputs: List[int] = None,
                 debug: bool = False):
        if program is not None:
            self.load_program(program)
        self.inputs = inputs or []
        self.outputs = []
        self.relative_base = 0
        self.debug = debug
        self.OPCODES = {
            1: self.addition,
            2: self.multiplication,
            3: self.take_input,
            4: self.output,
            5: self.jump_if_true,
            6: self.jump_if_false,
            7: self.less_than,
            8: self.equals,
            9: self.adjust_relative_base
        }

    def load_program(self, program: List[int]) -> int:
        self.program = program[:]
        self.instruction_pointer = 0
        return 0

    def set_inputs(self, inputs: List[int]) -> int:
        self.inputs += inputs
        return 0

    def execute(self) -> Tuple[str, int]:
        while self.program[self.instruction_pointer] != 99:
            instruction = self.program[self.instruction_pointer]
            decoded = IntcodeComputer.decode_instruction(instruction)
            opcode = decoded["opcode"]
            modes = decoded["modes"]

            if self.debug:
                print(opcode, modes)
            result = self.OPCODES[opcode](modes)

            if result == IntcodeComputer.RETURNING_OUTPUT:
                output = self.outputs.pop(0)
                return IntcodeComputer.RETURNING_OUTPUT, output
            elif result == IntcodeComputer.AWAITING_INPUT:
                return IntcodeComputer.AWAITING_INPUT, 0

        return IntcodeComputer.HALT, 0

    @staticmethod
    def decode_instruction(instruction: int) -> Dict:
        instruction_str = str(instruction)
        opcode = int(instruction_str[-2:])
        modes = [int(n) for n in instruction_str[:-2]]
        return {"opcode": opcode, "modes": modes}
    
    def write_to_memory(self, memory_location: int, value: int) -> int:
        assert memory_location >= 0, "Memory locations must be >= 0."

        try:
            self.program[memory_location] = value
        except IndexError:
            self.extend_memory(memory_location)
            self.write_to_memory(memory_location, value)

        return 0
    
    def extend_memory(self, memory_location: int) -> None:
        diff = memory_location - (len(self.program) - 1)
        self.program += [0 for _ in range(diff)]


    def addition(self, modes: List[int]) -> int:  # opcode 1
        a = self.get_value(1, IntcodeComputer.get_next_mode(modes))
        b = self.get_value(2, IntcodeComputer.get_next_mode(modes))
        memory_location = self.get_memory_location(3, IntcodeComputer.get_next_mode(modes))

        self.write_to_memory(memory_location, a+b)
        self.instruction_pointer += 4
        return 0

    def multiplication(self, modes: List[int]) -> int:  # opcode 2
        a = self.get_value(1, IntcodeComputer.get_next_mode(modes))
        b = self.get_value(2, IntcodeComputer.get_next_mode(modes))
        memory_location = self.get_memory_location(3, IntcodeComputer.get_next_mode(modes))
        
        self.write_to_memory(memory_location, a*b)
        
        self.instruction_pointer += 4
        return 0

    def take_input(self, modes: List[int]) -> Union[str, int]:  # opcode 3
        memory_location = self.get_memory_location(1, IntcodeComputer.get_next_mode(modes))
        next_input = self.get_next_input()
        if next_input == IntcodeComputer.AWAITING_INPUT:
            return IntcodeComputer.AWAITING_INPUT

        self.write_to_memory(memory_location, next_input)
        self.instruction_pointer += 2

        return 0

    def get_next_input(self) -> Union[str, int]:
        try:
            return self.inputs.pop(0)
        except IndexError:
            return IntcodeComputer.AWAITING_INPUT

    def output(self, modes: List[int]) -> int:  # opcode: 4
        output = self.get_value(1, IntcodeComputer.get_next_mode(modes))
        if self.debug:
            print("PROGRAM OUTPUT:", output)
        self.instruction_pointer += 2
        self.outputs.append(output)
        return IntcodeComputer.RETURNING_OUTPUT

    def jump_if_true(self, modes: List[int]) -> int:  # opcode 5
        value = self.get_value(1, IntcodeComputer.get_next_mode(modes))
        new_position = self.get_value(2, IntcodeComputer.get_next_mode(modes))
        if value != 0:
            self.instruction_pointer = new_position
        else:
            self.instruction_pointer += 3

        return 0

    def jump_if_false(self, modes: List[int]) -> int:  # opcode 6
        value = self.get_value(1, IntcodeComputer.get_next_mode(modes))
        new_position = self.get_value(2, IntcodeComputer.get_next_mode(modes))
        if value == 0:
            self.instruction_pointer = new_position
        else:
            self.instruction_pointer += 3
        return 0

    def less_than(self, modes: List[int]) -> int:  # opcode 7
        a = self.get_value(1, IntcodeComputer.get_next_mode(modes))
        b = self.get_value(2, IntcodeComputer.get_next_mode(modes))
        memory_location = self.get_memory_location(3, IntcodeComputer.get_next_mode(modes))

        self.write_to_memory(memory_location, int(a < b))
        self.instruction_pointer += 4

        return 0

    def equals(self, modes: List[int]) -> int:  # opcode 8
        a = self.get_value(1, IntcodeComputer.get_next_mode(modes))
        b = self.get_value(2, IntcodeComputer.get_next_mode(modes))
        memory_location = self.get_memory_location(3, IntcodeComputer.get_next_mode(modes))

        self.write_to_memory(memory_location, int(a == b))
        self.instruction_pointer += 4

        return 0
    
    def adjust_relative_base(self, modes: List[int]) -> int:  # opcode 9
        amount = self.get_value(1, IntcodeComputer.get_next_mode(modes))
        self.relative_base += amount
        self.instruction_pointer += 2
        return 0

    def get_value(self, position: int, mode: int) -> int:
        memory_location = self.get_memory_location(position, mode)
        
        try:
            return self.program[memory_location]
        except IndexError:
            self.extend_memory(memory_location)
            return self.get_value(position, mode)
    
    def get_memory_location(self, position: int, mode: int) -> int:
        if mode == 1:  # immediate mode
            return self.instruction_pointer + position
        elif mode == 2:  # relative mode
            return self.relative_base + self.program[self.instruction_pointer + position]
        else:  # position mode
            return self.program[self.instruction_pointer+position]

    @staticmethod
    def get_next_mode(modes: List[int]) -> int:
        try:
            return modes.pop()
        except IndexError:
            return 0

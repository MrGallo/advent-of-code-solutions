from typing import List, Tuple, Dict


class IntcodeComputer:
    def __init__(self, program: List[int], inputs: List[int], debug: bool = False):
        self.program = program[:]
        self.inputs = inputs
        self.instruction_pointer = 0
        self.debug = debug
        self.OPCODES = {
            1: self.addition,
            2: self.multiplication,
            3: self.take_input,
            4: self.output,
            5: self.jump_if_true,
            6: self.jump_if_false,
            7: self.less_than,
            8: self.equals
        }
    
    def get_next_input(self) -> int:
        try:
            return self.inputs.pop(0)
        except IndexError:
            raise IndexError("No more input to get.")
    
    def execute(self) -> int:
        while self.program[self.instruction_pointer] != 99:
            instruction = self.program[self.instruction_pointer]
            decoded = IntcodeComputer.decode_instruction(instruction)
            opcode = decoded["opcode"]
            modes = decoded["modes"]

            if self.debug:
                print(opcode, modes)
            self.OPCODES[opcode](modes)

        return self.program[0]
    
    @staticmethod
    def decode_instruction(instruction: int) -> Dict:
        instruction_str = str(instruction)
        opcode = int(instruction_str[-2:])
        modes = [int(n) for n in instruction_str[:-2]]
        return {"opcode": opcode, "modes": modes}
    
    def addition(self, modes: List[int]) -> None:
        a = self.get_value(1, IntcodeComputer.get_next_mode(modes))
        b = self.get_value(2, IntcodeComputer.get_next_mode(modes))
        output_position = self.program[self.instruction_pointer+3]

        self.program[output_position] = a + b
        self.instruction_pointer += 4

    def multiplication(self, modes: List[int]) -> None:
        a = self.get_value(1, IntcodeComputer.get_next_mode(modes))
        b = self.get_value(2, IntcodeComputer.get_next_mode(modes))

        output_position = self.program[self.instruction_pointer+3]
        self.program[output_position] = a * b
        self.instruction_pointer += 4

    def take_input(self, modes: List[int]) -> None:
        output_position = self.program[self.instruction_pointer+1]
        self.program[output_position] = self.get_next_input()
        self.instruction_pointer += 2

    def output(self, modes: List[int]) -> None:
        print("PROGRAM OUTPUT:", self.program[self.program[self.instruction_pointer+1]])
        self.instruction_pointer += 2

    def jump_if_true(self, modes: List[int]) -> None:
        value = self.get_value(1, IntcodeComputer.get_next_mode(modes))
        new_position = self.get_value(2, IntcodeComputer.get_next_mode(modes))
        if value != 0:
            self.instruction_pointer = new_position
        else:
            self.instruction_pointer += 3

    def jump_if_false(self, modes: List[int]) -> None:
        value = self.get_value(1, IntcodeComputer.get_next_mode(modes))
        new_position = self.get_value(2, IntcodeComputer.get_next_mode(modes))
        if value == 0:
            self.instruction_pointer = new_position
        else:
            self.instruction_pointer += 3

    def less_than(self, modes: List[int]) -> None:
        a = self.get_value(1, IntcodeComputer.get_next_mode(modes))
        b = self.get_value(2, IntcodeComputer.get_next_mode(modes))
        output_position = self.program[self.instruction_pointer+3]
        
        self.program[output_position] = int(a < b)
        self.instruction_pointer += 4

    def equals(self, modes: List[int]) -> None:
        a = self.get_value(1, IntcodeComputer.get_next_mode(modes))
        b = self.get_value(2, IntcodeComputer.get_next_mode(modes))
        output_position = self.program[self.instruction_pointer+3]

        self.program[output_position] = int(a == b)
        self.instruction_pointer += 4

    def get_value(self, position: int, mode: int) -> int:
        if mode == 1:
            return self.program[self.instruction_pointer+position]
        return self.program[self.program[self.instruction_pointer+position]]

    @staticmethod
    def get_next_mode(modes: List[int]) -> int:
        try:
            return modes.pop()
        except IndexError:
            return 0


def main() -> None:
    with open("input.txt", "r") as f:
        program = [int(n) for n in f.read().split(",")]
    
    # part 1
    computer = IntcodeComputer(program, inputs=[1])
    computer.execute()  # answer: 15386262

    # part 2
    computer = IntcodeComputer(program, inputs=[5])
    computer.execute()  # answer: 10376124


if __name__ == "__main__":
    main()
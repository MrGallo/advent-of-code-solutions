from itertools import permutations
from typing import List

from intcode_computer import IntcodeComputer


def main() -> None:
    with open("input.txt", "r") as f:
        amp_controller_code = [int(n) for n in f.read().split(",")]

    print(part1(amp_controller_code))  # answer: 19650
    print(part2(amp_controller_code))  # answer: 35961106


def part1(amp_controller_code: List[int]) -> int:
    output_signals = []
    for phase_setting_sequence in permutations(range(5), 5):
        amp_output = 0
        for setting in phase_setting_sequence:
            computer = IntcodeComputer(amp_controller_code,
                                       inputs=[setting, amp_output])
            code, amp_output = computer.execute()
        output_signals.append(amp_output)

    return max(output_signals)


def part2(amp_controller_code: List[int]) -> int:
    output_signals = []
    input_a = 0
    for phase_setting_sequence in permutations(range(5, 10), 5):
        a, b, c, d, e = phase_setting_sequence
        amp_computers = [
            IntcodeComputer(amp_controller_code, inputs=[a]),  # amp a
            IntcodeComputer(amp_controller_code, inputs=[b]),  # amp b
            IntcodeComputer(amp_controller_code, inputs=[c]),  # amp c
            IntcodeComputer(amp_controller_code, inputs=[d]),  # amp d
            IntcodeComputer(amp_controller_code, inputs=[e])   # amp e
        ]
        output = 0
        while True:
            return_codes = []
            for amp_comp in amp_computers:
                amp_comp.set_inputs([output])
                return_code, return_value = amp_comp.execute()
                if return_code == IntcodeComputer.RETURNING_OUTPUT:
                    output = return_value
                return_codes.append(return_code)
            if [IntcodeComputer.HALT] * 5 == return_codes:
                break

        output_signals.append(output)

    return max(output_signals)


if __name__ == "__main__":
    main()

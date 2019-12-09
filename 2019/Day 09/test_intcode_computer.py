from intcode_computer import IntcodeComputer


def test_adjust_relative_base():
    computer = IntcodeComputer()
    assert computer.relative_base == 0

    # immediate mode
    computer = IntcodeComputer([109, 5, 99])
    computer.execute()
    assert computer.relative_base == 5

    # position mode
    computer = IntcodeComputer([9, 3, 99, -7])
    computer.execute()
    assert computer.relative_base == -7


def test_get_value_relative():
    # base += 3 (immediate), output in relative mode
    computer = IntcodeComputer([109, 3, 204, 1, 99])
    code, result = computer.execute()
    assert computer.relative_base == 3
    assert result == 99

    computer = IntcodeComputer([109, 19, 204, -34, 99] + [n for n in range(5, 1996)])
    computer.relative_base = 2000
    code, result = computer.execute()
    assert computer.relative_base == 2019
    assert result == 1985


def test_extra_memory():
    # immediate mode, add 1 to 3, put in memory 5 (out of bounds)
    computer = IntcodeComputer([1101, 1, 3, 5, 99])
    computer.execute()
    assert computer.program[5] == 4


    computer = IntcodeComputer([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99], debug=True)
    code = 0
    while code != IntcodeComputer.HALT:
        code, result = computer.execute()

    computer = IntcodeComputer([1102,34915192,34915192,7,4,7,99,0])
    code, result = computer.execute()
    assert len(str(result)) == 16

    computer = IntcodeComputer([104,1125899906842624,99])
    code, result = computer.execute()
    assert result == 1125899906842624


def test_take_input():
    # position
    computer = IntcodeComputer([3, 0, 99], inputs=[1])
    computer.execute()
    print(computer.program)
    assert computer.program[0] == 1

    # immediate
    computer = IntcodeComputer([103, 5, 99], inputs=[4])
    computer.execute()
    assert computer.program[1] == 4

    # relative to 1, relative input to 1 is memory location 2
    computer = IntcodeComputer([9, 1, 203, 1, 99], inputs=[5])
    computer.execute()
    assert computer.program[2] == 5

def test_addition():
    # position output
    computer = IntcodeComputer([1101, 3, 5, 2, 99])
    computer.execute()
    assert computer.program[2] == 8

    # immediate
    computer = IntcodeComputer([11101, 3, 5, 2, 99])
    computer.execute()
    assert computer.program[3] == 8

    # relative
    computer = IntcodeComputer([109, -2, 21101, 5, 7, 4, 99])
    computer.execute()
    assert computer.relative_base == -2
    assert computer.program[2] == 12


def test_multiplication():
    # position output
    computer = IntcodeComputer([1102, 3, 5, 2, 99])
    computer.execute()
    assert computer.program[2] == 15

    # relative
    computer = IntcodeComputer([109, 2, 21102, 3, 5, 2, 99])
    computer.execute()
    assert computer.program[4] == 15


def test_less_than():
    # position output
    computer = IntcodeComputer([1107, 3, 5, 2, 99])
    computer.execute()
    assert computer.program[2] == 1

    # relative
    computer = IntcodeComputer([109, -1, 21107, 3, 5, 2, 99])
    computer.execute()
    assert computer.program[1] == 1


def test_equal():
    # position output
    computer = IntcodeComputer([1108, 3, 5, 2, 99])
    computer.execute()
    assert computer.program[2] == 0

    # relative
    computer = IntcodeComputer([109, -1, 21108, 3, 5, 3, 99])
    computer.execute()
    assert computer.program[2] == 0
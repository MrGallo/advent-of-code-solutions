from typing import List, Tuple, Callable, Optional


class BootCodeInterpreter:
    INFINITE_LOOP = "inf"
    COMPLETE = "done"
    OVERFLOW = "over"

    def __init__(self, code: Optional[List[Tuple[str, int]]] = None, debug: bool = False) -> None:
        self.code = None
        if code:
            self.code = self.compile(code)
        self.counter = 0
        self.pointer = 0
        self.debug = debug
        self.execution_counts = [0] * len(self.code) if self.code else 0
    
    def compile(self, code: List[Tuple[str, int]]) -> List[Tuple[Callable, int]]:
        FUNC_MAPPING = {
            'acc': self.acc,
            'jmp': self.jmp,
            'nop': self.nop
        }
        return [(FUNC_MAPPING[op], arg) for op, arg in code]

    def execute_next(self) -> None:
        func, value = self.code[self.pointer]
        if self.debug:
            print(f"{func.__name__}({value})")
        self.execution_counts[self.pointer] += 1
        func(value)
    
    def run(self) -> None:
        while self.pointer < len(self.code):
            if self.execution_counts[self.pointer] > 0:
                return BootCodeInterpreter.INFINITE_LOOP
            self.execute_next()

        if self.pointer == len(self.code):
            return BootCodeInterpreter.COMPLETE
        else:
            return BootCodeInterpreter.OVERFLOW

    def acc(self, value: int) -> None:
        self.counter += value
        self.pointer += 1

    def nop(self, value: int) -> None:
        self.pointer += 1

    def jmp(self, value: int) -> None:
        self.pointer += value


def main():
    with open('input.txt', 'r') as f:
        lines = [line for line in f.read().split("\n")]
        boot_code = []
        for line in lines:
            op, arg = line.split(" ")
            boot_code.append((op, int(arg)))

    bci = BootCodeInterpreter(boot_code)
    bci.run()
    print(bci.counter)  # Part 1: 1727

    for i, (op, value) in enumerate(boot_code):
        SWAP_MAP = {
            'jmp': 'nop',
            'nop': 'jmp',
            'acc': 'acc'
        }
        modification = [(SWAP_MAP[op], value)]
        modified_code = boot_code[:i] + modification + boot_code[i+1:]

        bci = BootCodeInterpreter(modified_code)
        result = bci.run()
        if result == BootCodeInterpreter.COMPLETE:
            break
    print(bci.counter)  # Part 2: 552


def tests():
    bci = BootCodeInterpreter()
    bci.acc(4)
    assert bci.counter == 4
    assert bci.pointer == 1

    bci.nop(56)
    assert bci.counter == 4
    assert bci.pointer == 2

    bci.jmp(-2)
    assert bci.pointer == 0


    source = [
        ('nop', 34),
        ('jmp', -3),
        ('acc', 4)
    ]
    bci = BootCodeInterpreter(source)
    assert bci.code == [(bci.nop, 34), (bci.jmp, -3), (bci.acc, 4)]

    source = [
        ('nop', 0),
        ('acc', 1),
        ('jmp', 4),
        ('acc', 3),
        ('jmp', -3),
        ('acc', -99),
        ('acc', 1),
        ('jmp', -4),
        ('acc', 6)
    ]
    bci = BootCodeInterpreter(source)

    bci.execute_next()
    assert bci.execution_counts[0] == 1

    bci = BootCodeInterpreter(source)
    result = bci.run()
    assert bci.counter == 5
    assert result == BootCodeInterpreter.INFINITE_LOOP

    bci = BootCodeInterpreter([('nop', 0)])
    result = bci.run()
    assert result == BootCodeInterpreter.COMPLETE

    bci = BootCodeInterpreter([('jmp', 2)])
    result = bci.run()
    assert result == BootCodeInterpreter.OVERFLOW

if __name__ == "__main__":
    tests()
    main()
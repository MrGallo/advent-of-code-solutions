from typing import List


def main() -> None:
    with open("input.txt", "r") as f:
        packages = [int(n) for n in f.read().split("\n")]

    options = get_compartment_options(packages, num_compartments=3)  # part 1
    products = [product(option) for option in options]
    print(min(products))  # answer: 11266889531

    options = get_compartment_options(packages, num_compartments=4)  # part 2
    products = [product(option) for option in options]
    print(min(products))  # answer: 77387711


def get_compartment_options(packages: List[int], num_compartments: int, target=None) -> List:
    if num_compartments == 1:
        if target is None or sum(packages) == target:
            return packages
        else:
            return []

    options = []
    for n in range(1, len(packages)):
        if options:
            break
        for compartment in select_packages(n, packages):
            # print(compartment)
            if target is None or sum(compartment) == target:
                remaining = [p for p in packages if p not in compartment]
                if sum(remaining) == sum(compartment) * (num_compartments-1):
                    sub_compartments = get_compartment_options(remaining, num_compartments-1, sum(compartment))
                    if sub_compartments:
                        options.append(compartment)
                        if target is not None:
                            break

    return options


def select_packages(n: int, packages: List[int]) -> List[int]:
    if n == 0:
        yield []
        return

    i = len(packages) - 1
    while i >= 0:
        for sub_combo in select_packages(n-1, packages[:i]):
            yield [packages[i]] + sub_combo
        i -= 1


def product(nums: List[int]) -> int:
    total = 1
    for n in nums:
        total *= n
    return total


if __name__ == "__main__":
    main()

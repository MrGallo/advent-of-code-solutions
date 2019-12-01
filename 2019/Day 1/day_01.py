
def fuel_requirement(mass: int) -> int:
    return mass // 3 - 2


def fuel_of_fuel_requirement(mass: int) -> int:
    total_fuel = 0
    while True:
        fuel_for_module = fuel_requirement(mass)
        if fuel_for_module < 1:
            return total_fuel
        total_fuel += fuel_for_module
        mass = fuel_for_module


with open('input.txt', 'r') as f:
    module_masses = [int(line) for line in f]


# part 1
print(sum([fuel_requirement(mass) for mass in module_masses]))  # answer: 3308377

# part 2
print(sum([fuel_of_fuel_requirement(mass) for mass in module_masses]))  # answer: 4959709

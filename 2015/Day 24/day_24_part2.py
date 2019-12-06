from typing import List


def select_packages(n: int, packages: List[int]) -> List[int]:
    if n == 0:
        yield []
        return

    i = len(packages) - 1
    while i >= 0:
        for sub_combo in select_packages(n-1, packages[:i]):
            yield [packages[i]] + sub_combo
        i -= 1


def can_be_balanced(combo: List[int], packages: List[int]) -> bool:
    remaining_packages = set(packages)
    compartment_1 = set(combo)
    # print(compartment_1)
    remaining_packages = list(remaining_packages - compartment_1)
    remaining_packages.sort()
    # print(remaining_packages)
    # input("pause")

    target = sum(compartment_1)
    # print(f"target: {target}")
    for n in range(1, len(remaining_packages)):
        for compartment_2 in select_packages(n, remaining_packages[:]):
            # print(f"container_2: {container_2}")
            compartment_2_weight = sum(compartment_2)
            compartment_3_weight = sum(remaining_packages) - compartment_2_weight
            # print("error:", target - container_2_weight)
            if compartment_2_weight == target:
                # print(f"container_1: {compartment_1}")
                # print(f"container_2: {compartment_2}")
                # input('pause')
                return True
        # input('pause')

    return False




    
    


with open("input.txt", "r") as f:
    packages = [int(n) for n in f.read().split("\n")]


print(packages)
payload_total_weight = sum(packages)
print(payload_total_weight)


compartment_1_options = []
for quantity in range(1, len(packages)//2):
    if compartment_1_options:
        break

    for compartment_1 in select_packages(quantity, packages[:]):
        compartment_1_weight = sum(compartment_1)
        remaining_weight = payload_total_weight - compartment_1_weight
        if remaining_weight == compartment_1_weight * 2 and can_be_balanced(compartment_1, packages[:]):
            compartment_1_options.append(compartment_1)
        elif remaining_weight > compartment_1_weight * 2:
            break

print(compartment_1_options)

def product(nums: List[int]) -> int:
    total = 1
    for n in nums:
        total *= n
    return total

qe_ratings = [product(package_weights) for package_weights in compartment_1_options]
print(min(qe_ratings))

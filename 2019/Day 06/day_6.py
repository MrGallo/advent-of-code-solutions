from collections import defaultdict
from typing import Dict, List

        
def main():
    with open('input.txt', 'r') as f:
        orbit_data = f.read().split("\n")

    part1(orbit_data)  # answer: 135690
    part2(orbit_data)  # answer: 298


def part1(orbit_data) -> None:
    orbit_map = compile_orbit_map(orbit_data)
    apply_orbit_counts(orbit_map)
    print(orbit_map["COM"][0][1])


def part2(orbit_data) -> None:
    orbit_map = compile_orbit_map(orbit_data)
    path_to_you = find_path_to("YOU", orbit_map)
    path_to_san = find_path_to("SAN", orbit_map)

    jumps_needed = len(path_to_you) + len(path_to_san)
    for loc_you, loc_san in zip(path_to_you, path_to_san):
        if loc_you != loc_san:
            break
        jumps_needed -= 2
    
    print(jumps_needed)


def compile_orbit_map(orbit_data):
    orbit_map = defaultdict(list)
    for datum in orbit_data:
        orbitee, orbitor = datum.split(")")
        orbit_map[orbitee].append(orbitor)
    return orbit_map


def apply_orbit_counts(orbit_map: Dict, current_location: str = "COM", depth: int = 0) -> None:
    if not orbit_map[current_location]:
        return depth
    
    orbitors_with_counts = []
    for orbitor in orbit_map[current_location]:
        orbit_count = apply_orbit_counts(orbit_map, orbitor, depth+1)
        orbitors_with_counts.append((orbitor, orbit_count))
    
    orbit_map[current_location] = orbitors_with_counts
    return depth + sum([count for loc, count in orbit_map[current_location]])


def find_path_to(target: str, orbit_map: Dict, current: str = "COM") -> List[str]:
    if len(orbit_map[current]) == 0:
        return None

    for orbitor in orbit_map[current]:
        if orbitor == target:
            return [current]
        potental_path = find_path_to(target, orbit_map, orbitor)
        if potental_path:
            return [current] + potental_path
    
    return None


if __name__ == "__main__":
    main()
from collections import defaultdict


def part_one():
    with open('input.txt') as f:
        reindeers = [parse_reindeer(line) for line in f]

    distances = [calc_distance_at(reindeer, 2503)
                 for reindeer in reindeers]
    print(max(distances))


def part_two():
    with open('input.txt') as f:
        reindeers = [parse_reindeer(line) for line in f]

    reindeer_points = [0] * len(reindeers)

    for second in range(1, 2503+1):
        distance_indicies = get_distance_indicies_at(reindeers, second)
        award_points(distance_indicies, reindeer_points)

    print(max(reindeer_points))


def parse_reindeer(line):
    words = line.split()
    name = words[0]
    fly_speed = int(words[3])
    fly_time = int(words[6])
    rest_time = int(words[13])
    return name, fly_speed, fly_time, rest_time


def calc_distance_at(reindeer, seconds):
    name, fly_speed, fly_time, rest_time = reindeer

    full_cycles = calc_num_cycles(seconds, fly_time, rest_time)
    remaining_time = calc_remaining_fly_time(seconds, fly_time, rest_time)

    return full_cycles * fly_time * fly_speed + remaining_time * fly_speed


def calc_num_cycles(seconds, fly_time, rest_time):
    return seconds // (fly_time + rest_time)


def calc_remaining_fly_time(seconds, fly_time, rest_time):
    return min(seconds % (fly_time + rest_time), fly_time)


def get_distance_indicies_at(reindeers, second):
    distance_indicies = defaultdict(list)
    for i, reindeer in enumerate(reindeers):
        distance = calc_distance_at(reindeer, second)
        distance_indicies[distance].append(i)
    return distance_indicies


def award_points(distance_indicies, reindeer_points):
    furthest_distance = max(distance_indicies.keys())
    for leader_index in distance_indicies[furthest_distance]:
        reindeer_points[leader_index] += 1


if __name__ == "__main__":
    part_one()  # answer: 2640
    part_two()  # answer: 1102

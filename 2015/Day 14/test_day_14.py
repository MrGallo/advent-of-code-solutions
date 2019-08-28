from day_14 import *

descriptions = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.""".split("\n")


def test_parse_reindeer_data():
    name, fly_speed, fly_time, rest_time = parse_reindeer(descriptions[0])
    assert name == "Comet"
    assert fly_speed == 14
    assert fly_time == 10
    assert rest_time == 127


def test_calc_num_cycles():
    name, fly_speed, fly_time, rest_time = parse_reindeer(descriptions[0])
    assert calc_num_cycles(1, fly_time, rest_time) == 0
    assert calc_num_cycles(11, fly_time, rest_time) == 0
    assert calc_num_cycles(10+127, fly_time, rest_time) == 1
    assert calc_num_cycles(10+127+1, fly_time, rest_time) == 1
    assert calc_num_cycles(10+127+10+127, fly_time, rest_time) == 2
    assert calc_num_cycles(10+127+10+127+11, fly_time, rest_time) == 2


def test_calc_remaining_time():
    name, fly_speed, fly_time, rest_time = parse_reindeer(descriptions[0])
    assert calc_remaining_fly_time(1, fly_time, rest_time) == 1
    assert calc_remaining_fly_time(11, fly_time, rest_time) == 10
    assert calc_remaining_fly_time(10 + 127, fly_time, rest_time) == 0
    assert calc_remaining_fly_time(10 + 127 + 5, fly_time, rest_time) == 5


def test_calc_distance_at():
    comet = parse_reindeer(descriptions[0])
    dancer = parse_reindeer(descriptions[1])
    assert calc_distance_at(comet, 1) == 14
    assert calc_distance_at(comet, 2) == 28
    assert calc_distance_at(comet, 10) == 14*10
    assert calc_distance_at(dancer, 10) == 16*10

    # no movement in rest period
    assert calc_distance_at(comet, 11) == 14*10

    # go for 10 seconds, rest for 127 seconds, go for one more second
    assert calc_distance_at(comet, 10 + 127 + 1) == 14*10 + 14


def test_acceptance_part_one():
    reindeers = [parse_reindeer(line) for line in descriptions]
    distances = [calc_distance_at(reindeer, 1000)
                 for reindeer in reindeers]
    assert max(distances) == 1120


def test_distance_indicies_at():
    reindeers = [parse_reindeer(line) for line in descriptions]
    distance_indicies = get_distance_indicies_at(reindeers, 1)
    assert distance_indicies == {14: [0], 16: [1]}

    distance_indicies = get_distance_indicies_at(reindeers, 2)
    assert distance_indicies == {28: [0], 32: [1]}


def test_award_points():
    reindeers = [parse_reindeer(line) for line in descriptions]
    reindeer_points = [0] * len(reindeers)

    for second in range(1, 139+1):
        distance_indicies = get_distance_indicies_at(reindeers, second)
        award_points(distance_indicies, reindeer_points)
        assert reindeer_points == [0, second]

    distance_indicies = get_distance_indicies_at(reindeers, 140)
    award_points(distance_indicies, reindeer_points)
    assert reindeer_points == [1, 139]


def test_acceptance_part_two():
    reindeers = [parse_reindeer(line) for line in descriptions]
    reindeer_points = [0] * len(reindeers)

    for second in range(1, 1000+1):
        distance_indicies = get_distance_indicies_at(reindeers, second)
        award_points(distance_indicies, reindeer_points)

    assert reindeer_points == [312, 689]

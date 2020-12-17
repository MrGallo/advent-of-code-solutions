def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        earliest = int(lines[0].strip())
        busses_str = [id for id in lines[1].strip().split(",")]
    
    bus_ids = [int(n) for n in busses_str if n != 'x']    
    cycles = [earliest // id for id in bus_ids]
    
    wait_times = {}
    shortest = None
    for cycle, b_id in zip(cycles, bus_ids):
        departing = cycle * b_id
        while departing < earliest:
            departing += b_id
        
        wait_time = departing - earliest
        if shortest is None or wait_time < shortest[1]:
            shortest = (b_id, wait_time)
        wait_times[b_id] = wait_time
    
    b_id, wait_time = shortest
    print(b_id * wait_time)  # Part 1: 102

    bus_ids_order = [(i, int(n)) for i, n in enumerate(busses_str) if n != 'x']

    t = 100000000000000
    in_order = False
    while not in_order:
        t += 1
        in_order = True
        for offset, b_id in bus_ids_order:
            if (t + offset) % b_id != 0:
                in_order = False
    
    print(t)


def tests():
    pass


if __name__ == "__main__":
    tests()
    main()
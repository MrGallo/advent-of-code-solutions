# Day 0: 
import re
import datetime
import numpy as np

def parse_entry(string):
    year, month, day = [int(n) for n in re.search(r'\[([0-9]{4}\-[0-9]{2}\-[0-9]{2})', string).group(1).split('-')]
    hour, minute = [int(n) for n in re.search(r'([0-9]{2}\:[0-9]{2})\]', string).group(1).split(':')]
    record = re.search(r'\] (.*)$', string).group(1)
    return (datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute), record)


def sort_dates_asc(entries):
    return sorted(entries)


def mutate_with_id(entries):
    """Must be sorted entries by datetime asc"""
    entries = sort_dates_asc(entries)
    
    new_entries = []
    current_id = None
    for i, (date, record) in enumerate(entries):
        try:
            entry_id = int(re.search(r'([0-9]+)', record).group(1))
        except:
            # just a record here, add current id to tuple.
            new_entries.append((current_id, date, record))
        else:
            # first entry for the day, get id and replace record
            new_record = re.search(r'[0-9]+ (.*)', record).group(1)
            current_id = entry_id
            new_entries.append((current_id, date, new_record))
    
    return new_entries
        

def plot_sleep_chart(entries):
    time_chart = None
    sleep_begins = 0
    current_row = 0
    for e_id, date, record in entries:
        if record == "begins shift":
            if time_chart is None:
                time_chart = np.zeros((1, 60), dtype=int)
            else:
                time_chart = np.append(time_chart, np.zeros((1, 60), dtype=int), axis=0)
                current_row += 1
        elif record == "falls asleep":
            sleep_begins = date.minute
        elif record == "wakes up":
            sleep_ends = date.minute
            time_chart[current_row:, sleep_begins:sleep_ends] = e_id
    return time_chart

def main():
    print("Day 4: ")
    
    print("Part 1:")
    
    with open('input.txt') as f:
        entries = [parse_entry(entry) for entry in f]
    
    entries = mutate_with_id(entries)
    time_chart = plot_sleep_chart(entries)

    # count highest occurance of particular ids -> id with most sleep time
    ids, counts = np.unique(time_chart, return_counts=True)
    sleep_counts = sorted(list(zip(ids, counts))[1:], key=lambda x: x[1])
    biggest_sleeper, minutes = sleep_counts[-1]
    
    only_biggest_sleeper = time_chart[~np.all(time_chart != biggest_sleeper, axis=1)]
    np.set_printoptions(threshold=np.nan)
    
    minute = 0
    max_val = 0
    for i, total in enumerate(sum(only_biggest_sleeper)):
        
        if total > max_val:
            minute = i
            max_val = total

    print(minute * biggest_sleeper)
    
    print("Part 2:")
    
    ids = ids[1:]
    guard_id_max = 0
    most_slept_minute = None
    times_slept_max = 0
    for guard in ids:
        guard_only_chart = np.clip(time_chart[~np.all(time_chart != guard, axis=1)], a_max=1, a_min=0)
        for m, total in enumerate(sum(guard_only_chart)):
            if total > times_slept_max:
                times_slept_max = total
                guard_id_max = guard
                most_slept_minute = m
    
    print(guard_id_max * most_slept_minute)
    
        

if __name__ == "__main__":
    main()
    
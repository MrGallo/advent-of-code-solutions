# Day 2: Inventory Management System


def file_to_list(test_file, datatype=int):
        with open(test_file) as f:
            return [datatype(line) for line in f]


def get_count(id):
    
    
    counts = {}
    for letter in id:
        if counts.get(letter):
            counts[letter] += 1
        else:
            counts[letter] = 1
    
    double = int(2 in counts.values())
    triple = int(3 in counts.values())
    return (double, triple)


def get_diffs(id1, id2):
    return [int(a!=b) for a, b in zip(id1, id2)]


def find_match(ids):
    count = 0
    for i in range(len(ids)):
        current = ids[i]
        for other in ids[i:]:
            diffs = get_diffs(current, other)
            if sum(diffs) == 1:
                return (current, other)

def main():
    print("Day 2: Inventory Management System")
    
    print("Part 1:")
    total_double, total_triple = 0, 0
    
    with open("input.txt") as f:
        for line in f:
            double, triple = get_count(line)
            total_double += double
            total_triple += triple
            
    print(total_double*total_triple)
    
    
    print("Part 2:")
    with open("input.txt") as f:
        ids = [line.strip() for line in f]
    
    id1, id2 = find_match(ids)
    diffs = get_diffs(id1, id2)
    diff_index = diffs.index(1)
    
    similar = list(id1)
    similar.pop(diff_index)
    
    print("".join(similar))
                
        

if __name__ == "__main__":
    main()
    
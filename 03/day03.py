import re
import numpy as np

# Day 3: No Matter How You Slice It

def get_end_point(start_point, size):
    x, y = start_point
    width, height = size
    end_point = x + width - 1, y + height - 1
    return end_point


def parse_claim(string):
    claim_id = int(re.search(r'\#([0-9]+)\s', string).group(1))
    start_point = tuple(int(n) for n in re.search(r'\@ ([0-9]+,[0-9]+):', string).group(1).split(","))
    width, height = tuple(int(n) for n in re.search(r'\: ([0-9]+x[0-9]+)', string).group(1).split("x"))
    x, y = start_point
    end_point = x + width - 1, y + height - 1
    return (claim_id, start_point, end_point)
    
    
def get_claim_roi(claim):
    claim_id, start_point, end_point = claim
    x1, y1 = start_point
    x2, y2 = end_point
    
    return np.index_exp[y1:y2+1, x1:x2+1]
    

def main():
    print("Day 3: No Matter How You Slice It")
    
    print("Part 1:")
    sheet = np.zeros((1000,1000), dtype=int)
    
    with open('input.txt') as f:
        claims = [parse_claim(line) for line in f]
    
    for claim in claims:
        roi = get_claim_roi(claim)
        sheet[roi] += 1
    
    # get sum
    total = np.count_nonzero(sheet > 1)
    print(total)
    
    print("Part 2:")
    
    # get non overlaping claim
    non_overlaping_claim = None
    for claim in claims:
        claim_id, _, _ = claim
        roi = get_claim_roi(claim)
        
        if np.count_nonzero(sheet[roi] > 1) == 0:
            non_overlaping_claim = claim_id
            break
                
    print(non_overlaping_claim)

if __name__ == "__main__":
    main()
    
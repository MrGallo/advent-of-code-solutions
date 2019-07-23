import os

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)


def wrapping_paper_needed(box_list):
    """Part 1"""

    total = 0
    for l, w, h in box_list:
        side_a = l*w
        side_b = w*h
        side_c = h*l

        smallest_side = min(side_a, side_b, side_c)

        total += 2*side_a + 2*side_b + 2*side_c + smallest_side
    return total


def ribbon_needed(box_list):
    """Part 2"""

    total = 0
    for l, w, h in box_list:
        face_a = 2*l + 2*w
        face_b = 2*w + 2*h
        face_c = 2*h + 2*l

        volume = l*w*h
        smallest_perimeter = min(face_a, face_b, face_c)

        total += smallest_perimeter + volume
    return total


with open('input.txt', 'r')as f:
    box_list = [
        tuple(map(int, box.split('x')))
        for box in f.read().split("\n")
        if box
    ]

print(wrapping_paper_needed(box_list))  # result: 1588178
print(ribbon_needed(box_list))  # result: 3783758

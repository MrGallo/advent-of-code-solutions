from collections import Counter

def manhatten_dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    
    x_dist = abs(x2-x1)
    y_dist = abs(y2-y1)
    return x_dist + y_dist
    

def part1():
    # infinite area are those with closest distances at the border of the matrix
    infinite_area_coords = set()
    
    # top
    for point_list, distance in distance_matrix[0]:
        if len(point_list) == 1:
            point = point_list[0]
            infinite_area_coords.add(point)
    
    # bottom
    for point_list, distance in distance_matrix[-1]:
        if len(point_list) == 1:
            point = point_list[0]
            infinite_area_coords.add(point)
    
    # left
    for row in distance_matrix:
        point_list, distance = row[0]
        if len(point_list) == 1:
            point = point_list[0]
            infinite_area_coords.add(point)
    
    # right
    for row in distance_matrix:
        point_list, distance = row[-1]
        if len(point_list) == 1:
            point = point_list[0]
            infinite_area_coords.add(point)
    
    
    coord_areas = Counter()
    for row in distance_matrix:
        for point_list, distance in row:
            if len(point_list) == 1:
                closest_point = point_list[0]
                if closest_point not in infinite_area_coords:
                    coord_areas[closest_point] += 1
    
    print(coord_areas.most_common())
    

coords = [tuple(map(int, line.split(', '))) for line in open('input.txt').read().split('\n')]

# coords = [
#     (2, 2),
#     (4, 2)
# ]

# populate closest distance list
left_most_coord = max(coords, key=lambda t: t[0])
right_most_coord = min(coords, key=lambda t: t[0])

upper_most_coord = min(coords, key=lambda t: t[1])
lower_most_coord = max(coords, key=lambda t: t[1])

width = left_most_coord[0] + 1
height = lower_most_coord[1] + 1

# distance_matrix = []
total_distances = Counter()

for y in range(height):
    for x in range(width):
        current_point = x, y
        for coord in coords:
            distance = manhatten_dist(current_point, coord)
            total_distances[current_point] += distance

total_points_within_range = 0
for point, distance in total_distances.items():
    if distance < 10000:
        total_points_within_range += 1

print(total_points_within_range)

# for y in range(height):
#     row = []
#     for x in range(width):
#         current_point = x, y
#         closest_coord = (
#             [coords[0]],
#             manhatten_dist(current_point, coords[0])
#         )
#         for coord in coords[1:]:
#             current_dist = manhatten_dist(current_point, coord)
#             if  current_dist < closest_coord[1]:
#                 closest_coord = ([coord], current_dist)
#             elif current_dist == closest_coord[1]:
#                 # print("tie")
#                 closest_coord[0].append(coord)

#         row.append(closest_coord)
#     distance_matrix.append(row)


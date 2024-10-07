from functions import draw_line, find_sand_pos

input = [line.strip().split(" -> ") for line in open("Day 14/rawData.txt")]
data = []
for line in input:
    temp_line = []
    for pos in line:
        temp_line.append(eval(pos))
    data.append(temp_line)

points = []
for line in data:
    for index, point in enumerate(line[1:]):
        for item in draw_line(point, line[index]):
            if item not in points: points.append(item)

max_y = 0
for point in points:
    if point[1] > max_y: max_y = point[1]

for item in draw_line((0, max_y+2), (1000, max_y+2)): points.append(item)

sand_total = 1
cur_sand_pos = (500, 0)

#print(points)

while (500, 0) not in points:
    sand_stopped, cur_sand_pos = find_sand_pos(cur_sand_pos, points)
    if sand_stopped:
        #print(f"sand #{sand_total} stopped at {cur_sand_pos}")
        points.append(cur_sand_pos)
        sand_total += 1
        cur_sand_pos = (500, 0)
        sand_stopped = False
        if sand_total % 10 == 0:
            print(f"total sand: {sand_total}")


print(sand_total-1)
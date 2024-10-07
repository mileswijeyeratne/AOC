data = []
for line in open("Day 15/rawData.txt"):
    line = line.strip().split(" ")
    sensor_x = int(line[2][:-1].lstrip("x="))
    sensor_y = int(line[3][:-1].lstrip("y="))
    beacon_x = int(line[-2][:-1].lstrip("x="))
    beacon_y = int(line[-1].lstrip("y="))
    data.append(((sensor_x, sensor_y),(beacon_x, beacon_y)))

impossible_positions = []
row_to_count = 2000000

for sensor_pos, beacon_pos in data:
    d_x = abs(sensor_pos[0] - beacon_pos[0])
    d_y = abs(sensor_pos[1] - beacon_pos[1])
    d_total = d_x + d_y
    d_possible = d_total
    if abs(sensor_pos[1] - row_to_count) < d_possible:
        distance_y = abs(sensor_pos[1] - row_to_count)
        x_possible = d_possible - distance_y
        min_x = sensor_pos[0] - x_possible
        max_x = sensor_pos[0] + x_possible + 1
        for x in range(min_x, max_x):
            if (x, row_to_count) != sensor_pos and (x, row_to_count) != beacon_pos:
                impossible_positions.append((x, row_to_count))

print(len(set(impossible_positions)))

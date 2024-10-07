from time import time

max_searh_space = 4_000_000

data = []
for line in open("Day 15/rawData.txt"):
    line = line.strip().split(" ")
    sensor_x = int(line[2][:-1].lstrip("x="))
    sensor_y = int(line[3][:-1].lstrip("y="))
    beacon_x = int(line[-2][:-1].lstrip("x="))
    beacon_y = int(line[-1].lstrip("y="))
    data.append(((sensor_x, sensor_y),(beacon_x, beacon_y)))

def find_diamond_points(center, size, search_size):
    count = 0
    x, y = center
    points = []
    for i in range(x-size, x+size+1):
        for j in range(y-size, y+size+1):
            dx = abs(x - i)
            dy = abs(y - j)
            if dx+dy <= size and i >= 0 and i <= search_size and j <= search_size and j >= 0:
                points.append((i, j))
            count += 1
            if count % 1_000_000 == 0:
                print(f"{count} points processed")
    return points

#max_searh_space = 4000000
#possible_beacon_spots = []
#for i in range(max_searh_space+1):
#    for j in range(max_searh_space+1):
#        possible_beacon_spots.append((i, j))


impossible_positions = []
for index, (sensor_pos, beacon_pos) in enumerate(data):
    start = time()
    print(f"processing beacon {index+1}/{len(data)}")
    d_x = abs(sensor_pos[0] - beacon_pos[0])
    d_y = abs(sensor_pos[1] - beacon_pos[1])
    d_total = d_x + d_y
    impossible_positions.extend(find_diamond_points(sensor_pos, d_total, max_searh_space))
    print(f"beacon {index+1}/{len(data)} processed in {time() - start} seconds")

possible_beacon_spots = []
start = time()
print("finding solution")
for i in range(max_searh_space+1):
    for j in range(max_searh_space+1):
        if (i*max_searh_space + j) % 50 == 0:
            print(f"{i*max_searh_space + j}/{max_searh_space**2}")
        if not (i, j) in impossible_positions:
            possible_beacon_spots.append((i, j))
print(f"solution found in {time() - start} seconds")
    



print(possible_beacon_spots)
print(len(possible_beacon_spots))
print(possible_beacon_spots[0][0]*4000000+possible_beacon_spots[0][1])
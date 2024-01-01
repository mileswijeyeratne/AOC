from time import time

max_search_space = 4_000_000

data = []
for line in open("Day 15/rawData.txt"):
    line = line.strip().split(" ")
    sensor_x = int(line[2][:-1].lstrip("x="))
    sensor_y = int(line[3][:-1].lstrip("y="))
    beacon_x = int(line[-2][:-1].lstrip("x="))
    beacon_y = int(line[-1].lstrip("y="))
    d_x = abs(sensor_x - beacon_x)
    d_y = abs(sensor_y - beacon_y)
    d_total = d_x + d_y
    data.append(((sensor_x, sensor_y),(beacon_x, beacon_y), d_total))


def check_possible(point):
    x, y = point
    for (sensor_x, sensor_y), _, dist in data:
        d_x = abs(sensor_x - x)
        d_y = abs(sensor_y - y)
        d_total = d_x + d_y
        if d_total <= dist:
            return False
    return True

found = []
start = time()
last = start
for i in range(3915, max_search_space+1):
    for j in range(max_search_space+1):
        if check_possible((i, j)):
            found.append((i, j))
            print(f"({i}, {j}) added to possible points")
        if (i*max_search_space + j) % 1_000_000 == 0:
            print(f"{i*max_search_space + j:,}/{max_search_space**2:,} points processed in {time()-start} seconds")
            print(f"last 1,000,000 points processsed in {time()-last} seconds")
            print(f"{len(found)} points founds")
            if len(found) > 0: print(found[0])
            print("")
            last = time()

if len(found) < 10:
    print(found)
else:
    print(found[:10])
print(found[0][0]*4_000_000+found[0][1])
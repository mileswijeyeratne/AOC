from functions import getDirections

data = [eval(line.strip()) for line in open("Day 18/rawData.txt")]

total_sa = 0
for index, cube in enumerate(data):
    if index % 25 == 0: print(f"cube {index}/{len(data)}")
    sa = 6
    for direction in getDirections(cube):
        if direction in data:
            sa -= 1
    total_sa += sa

print(total_sa)
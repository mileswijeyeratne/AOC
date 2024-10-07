from funcitons import vectorAdd

data = [line.strip() for line in open("Day 23/rawData.txt")]

elves = []
for row_ind, row in enumerate(data):
    for col_ind, char in enumerate(row):
        if char == "#":
            elves.append((row_ind, col_ind))
    
directions = {
    "N": (-1, 0),
    "S": (1, 0),
    "E": (0, 1),
    "W": (0, -1),
    "NE": (-1, 1),
    "NW": (-1, -1),
    "SE": (1, 1),
    "SW": (1, -1)
}

positions_to_check = [
    ["N", "NE", "NW"],
    ["S", "SE", "SW"],
    ["W", "NW", "SW"],
    ["E", "NE", "SE"]
]

def calculate_directions(elves):
    positions = []
    for elf in elves:
        target_pos = elf
        adjacent_elf = False
        for direction in directions:
            if vectorAdd(elf, directions[direction]) in elves:
                adjacent_elf = True
        if not adjacent_elf: target_pos = elf
        elif (not vectorAdd(elf, directions[positions_to_check[0][0]]) in elf) and (not vectorAdd(elf, directions[positions_to_check[0][1]]) in elf) and (not vectorAdd(elf, directions[positions_to_check[0][2]]) in elf):
            target_pos = vectorAdd(target_pos, directions[positions_to_check[0][0]])
        elif (not vectorAdd(elf, directions[positions_to_check[1][0]]) in elf) and (not vectorAdd(elf, directions[positions_to_check[1][1]]) in elf) and (not vectorAdd(elf, directions[positions_to_check[1][2]]) in elf):
            target_pos = vectorAdd(target_pos, directions[positions_to_check[1][0]])
        elif (not vectorAdd(elf, directions[positions_to_check[2][0]]) in elf) and (not vectorAdd(elf, directions[positions_to_check[2][1]]) in elf) and (not vectorAdd(elf, directions[positions_to_check[2][2]]) in elf):
            target_pos = vectorAdd(target_pos, directions[positions_to_check[2][0]])
        elif (not vectorAdd(elf, directions[positions_to_check[3][0]]) in elf) and (not vectorAdd(elf, directions[positions_to_check[3][1]]) in elf) and (not vectorAdd(elf, directions[positions_to_check[3][2]]) in elf):
            target_pos = vectorAdd(target_pos, directions[positions_to_check[3][0]])
        else: target_pos = elf
        positions.append(target_pos)
    return positions

def move_elves(elves, target_positions):
    new_elves = elves
    for index, elf in enumerate(elves):
        temp_list = [item for item in target_positions]
        if elf not in temp_list:
            new_elves[index] = target_positions[index]
        else: new_elves[index] = elves[index]
    
    return new_elves

def find_empty_squares(elves):
    max_row = 0
    min_row = 0
    max_col = 0
    min_col = 0
    for elve in elves:
        if elve[0] > max_row:
            max_row = elve[0]
        elif elve[0] < min_row:
            min_row = elve[0]
        if elve[1] > max_col:
            max_col = elve[1]
        elif elve[1] < min_col:
            min_col = elve[1]
    d_row = max_row - min_row + 1
    d_col = max_col - min_col + 1
    total_squares = d_row * d_col
    return total_squares - len(elves)

for _ in range(10):
    target_directions = calculate_directions(elves)
    elves = move_elves(elves, target_directions)
    positions_to_check.append(positions_to_check[0])
    positions_to_check.pop(0)

print(elves)
print(find_empty_squares(elves))
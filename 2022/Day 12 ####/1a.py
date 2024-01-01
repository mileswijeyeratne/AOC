input = [line.strip() for line in open("Day 12/rawData.txt")]

start = []
target = []
step_map = []
height_map = []
for row_ind, line in enumerate(input):
    temp_height_line = []
    temp_step_line = []
    for col_ind, char in enumerate(line):
        if char == "S":
            start = [row_ind, col_ind]
            char = "a"
        elif char == "E":
            target = [row_ind, col_ind]
            char = "z"
        temp_height_line.append(ord(char)-97)
        temp_step_line.append("#")
    step_map.append(temp_step_line)
    height_map.append(temp_height_line)
current_pos = start

def find_directions(pos, map):
    directions = []
    directions.append([pos[0]+1, pos[1]])
    directions.append([pos[0], pos[1]+1])
    directions.append([pos[0]-1, pos[1]])
    directions.append([pos[0], pos[1]-1])
    dir_to_return = []
    for direction in directions:
        if not (direction[0] < 0 or direction[1] < 0 or direction[0] >= len(map) or direction[1] >= len(map[0])):
            dir_to_return.append(direction)
    return dir_to_return

while start != target:
    steps = step_map[current_pos[0]][current_pos[1]]
    potential_direcitons = find_directions(start, height_map)
    possible_directions = []
    for direction in potential_direcitons:
        if  abs(height_map[direction[0]][direction[1]] - height_map[current_pos[0]][current_pos[1]]) <= 1:
            possible_directions.append(direction)
    direction_found = False
    direction_picked = []
    for direcion in possible_directions:
        if step_map[direction[0]][direction[1]] == "#":
            direction_found = True
            direction_picked = direction
            break
    
    
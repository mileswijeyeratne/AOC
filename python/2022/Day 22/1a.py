data = [line.strip("\n") for line in open("Day 22/rawData.txt")]
map = []
input_str = ""
input = []
section = "map"
for line in data:
    if line == "":
        section = "input"
    elif section == "map":
        line_to_add = []
        for char in line:
            if char == " ":
                line_to_add.append("o")
            else: line_to_add.append(char)
        while len(line_to_add) < 150:
            line_to_add.append("o")
        map.append(line_to_add)
    elif section == "input":
        input_str = input_str + line
command = ""
for char in input_str:
    if not char.isnumeric():
        input.append(int(command))
        command = ""
        input.append(char)
    else:
        command = command + char
input.append(int(command))


#do all calculations starting counting from 0
#calculate final code with start at 1

row, col = 0, 0
#facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
facing = 0
for index, char in enumerate(map[row]):
    if char == ".":
        col = index
        break

def can_move_forward(facing, row, col, map):
    # find the square to check
    if facing == 0:
        col_to_check = col
        row_to_check = row+1
        if row_to_check >= len(map):
            row_to_check -= len(map)
        temp_map = map
        for _ in range(row_to_check):
            temp_map.append(temp_map[0])
            temp_map.pop(0)
        for index, row in enumerate(temp_map):
            if row[col_to_check] != "o":
                row_to_check += index
                break
        if row_to_check >= len(map):
            row_to_check -= len(map)
    
    elif facing == 1:
        col_to_check = col+1
        row_to_check = row
        if col_to_check >= len(map[row_to_check]):
            col_to_check -= len(map[row_to_check])
        temp_row = map[row_to_check]
        for _ in range(col_to_check):
            temp_row.append(temp_row[0])
            temp_row.pop(0)
        for index, char in enumerate(temp_row):
            if char != "o":
                row_to_check += index
                break
        if col_to_check >= len(map[row_to_check]):
            col_to_check -= len(map[row_to_check])

    elif facing == 2:
        col_to_check = col
        row_to_check = row-1
        if row_to_check < 0:
            row_to_check += len(map)
        temp_map = map
        for _ in range(len(map) - row_to_check):
            temp_map.insert(0, temp_map[-1])
            temp_map.pop()
        temp_map = temp_map[::-1]
        for index, row in enumerate(temp_map):
            if row[col_to_check] != "o":
                row_to_check -= index
                break
        if row_to_check < 0:
            row_to_check += len(map)
    
    elif facing == 4:
        col_to_check = col-1
        row_to_check = row
        if col_to_check < 0:
            col_to_check += len(map[row_to_check])
        temp_row = map[row_to_check]
        for _ in range(len(row_to_check) - col_to_check):
            temp_row.insert(0, temp_row[-1])
            temp_row.pop()
        temp_row = temp_row[::-1]
        for index, char in enumerate(temp_row):
            if char != "o":
                row_to_check -= index
                break
        if col_to_check < 0:
            col_to_check += len(map[row_to_check])

    # check if square is "#"
    if map[row_to_check][col_to_check] == "#":
        return False, None
    else:
        return True, (row_to_check, col_to_check)


for move in input:
    if move == "L":
        facing -= 1
        if facing == -1:
            facing = 3
    elif move == "R":
        facing += 1
        if facing == 4:
            facing = 0
    else:
        can_move, move_to = can_move_forward(facing, row, col, map)
        cycles = 0
        while can_move and cycles < move:
            print(row, col)
            cycles += 1
            row, col = move_to
            can_move, move_to = can_move_forward(facing, row, col, map)

# The final password is the sum of 1000 times the row, 4 times the column, and the facing

row_from_1 = row + 1
col_from_1 = col + 1

print(1000*row_from_1 + 4*col_from_1 + facing)
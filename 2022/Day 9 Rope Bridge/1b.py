data = [line.strip().split(" ") for line in open("Day 9/rawData.txt")]
input = []
for line in data:
    for i in range(int(line[1])):
        input.append(line[0])


def solve(x):
    space = [["HT"]]
    directions = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}
    squares = []
    def change_suqare_index(index):
        for square in squares:
            square[index] += 1
    
    head_pos = None
    tail_positions = {}
    for row_ind, row in enumerate(space):
        for col_ind, pos in enumerate(row):
                if "H" in pos:
                    head_pos = [row_ind, col_ind]
                    space[row_ind][col_ind] = space[row_ind][col_ind].replace("H", "")
                for i in range(1, 10):
                    if str(i) in pos:
                        tail_positions[str(i)] = [row_ind, col_ind]
                        space[row_ind][col_ind] = space[row_ind][col_ind].replace(str(i), "")

    for line in input:
        
        
        # UPDATE SPACE SIZE
        direction_to_move = directions[line]
        if head_pos[0] + direction_to_move[0] > len(space) - 1:
            #add extra row to space
            row_to_append = []
            for i in range(len(space[0])):
                row_to_append.append("")
            space.append(row_to_append)
        if head_pos[1] + direction_to_move[1] > len(space[0]) - 1:
            #add extra column to each row in space
            for row in space:
                row.append("")
        if head_pos[0] + direction_to_move[0] < 0:
            #add row before and increase head and tail row index
            row_to_append = []
            for i in range(len(space[0])):
                row_to_append.append("")
            space.insert(0, row_to_append)
            head_pos[0] += 1
            for _, item in tail_positions.items():
                item[0] += 1
            change_suqare_index(0)
        if head_pos[1] + direction_to_move[1] < 0:
            #add column before and increase head and tail column index
            for row in space:
                row.insert(0, "")
            head_pos[1] += 1
            for _, item in tail_positions.items():
                item[1] += 1
            change_suqare_index(1)

        # MOVE HEAH
        head_pos[0] += direction_to_move[0]
        head_pos[1] += direction_to_move[1]

        #MOVE TAIL
        for key, item in tail_positions.items():
            # special case for first item
            moved_x = False
            moved_y = False
            if key == 1:
                check_relative = head_pos
            else: check_relative = tail_positions[str(int(key)+1)]
            if abs(head_pos[0] - item[0]) > 1:
                # change tail row
                if check_relative[0] - item[0] > 0:
                    item[0] += 1
                else:
                    item[0] -= 1
                moved_x = True
            if abs(check_relative[1] - item[1]) > 1:
                #change tail col
                if check_relative[1] - item[1] > 0:
                    item[1] += 1
                else:
                    item[1] -= 1
                moved_y = True
            if moved_x and check_relative[1] != item[1]:
                if check_relative[1] - item[1] > 0:
                    item[1] += 1
                else: item[1] -= 1
            if moved_y and check_relative[0] != item[0]:
                if check_relative[0] - item[0] > 0:
                    item[0] += 1
                else: item[0] -= 1

            if key == "9":
                if item not in squares:
                    squares.append(item)

        # UPDATE SPACE
        space[head_pos[0]][head_pos[1]] = space[head_pos[0]][head_pos[1]] + "H"
        for key, item in tail_positions.items():
            space[item[0]][item[1]] = space[item[0]][item[1]] + key
        

    return len(squares)

print(solve(input)) 
data = [line.strip().split(" ") for line in open("Day 9 Rope Bridge/rawData.txt")]
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

    for line in input:
        head_pos = None
        tail_pos = None
        for row_ind, row in enumerate(space):
            for col_ind, pos in enumerate(row):
                    if "H" in pos:
                        head_pos = [row_ind, col_ind]
                        space[row_ind][col_ind] = space[row_ind][col_ind].replace("H", "")
                    if "T" in pos:
                        tail_pos = [row_ind, col_ind]
                        space[row_ind][col_ind] = space[row_ind][col_ind].replace("T", "")
        
        
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
            tail_pos[0] += 1
            change_suqare_index(0)
        if head_pos[1] + direction_to_move[1] < 0:
            #add column before and increase head and tail column index
            for row in space:
                row.insert(0, "")
            head_pos[1] += 1
            tail_pos[1] += 1
            change_suqare_index(1)

        # MOVE HEAH
        head_pos[0] += direction_to_move[0]
        head_pos[1] += direction_to_move[1]

        #MOVE TAIL
        moved_x = False
        moved_y = False
        if abs(head_pos[0] - tail_pos[0]) > 1:
            # change tail row
            if head_pos[0] - tail_pos[0] > 0:
                tail_pos[0] += 1
            else:
                tail_pos[0] -= 1
            moved_x = True
        if abs(head_pos[1] - tail_pos[1]) > 1:
            #change tail col
            if head_pos[1] - tail_pos[1] > 0:
                tail_pos[1] += 1
            else:
                tail_pos[1] -= 1
            moved_y = True
        if moved_x and head_pos[1] != tail_pos[1]:
            if head_pos[1] - tail_pos[1] > 0:
                tail_pos[1] += 1
            else: tail_pos[1] -= 1
        if moved_y and head_pos[0] != tail_pos[0]:
            if head_pos[0] - tail_pos[0] > 0:
                tail_pos[0] += 1
            else: tail_pos[0] -= 1
        if tail_pos not in squares:
            squares.append(tail_pos)


        # UPDATE SPACE
        space[head_pos[0]][head_pos[1]] = space[head_pos[0]][head_pos[1]] + "H"
        space[tail_pos[0]][tail_pos[1]] = space[tail_pos[0]][tail_pos[1]] + "T"
        

    return len(squares)

print(solve(input)) 
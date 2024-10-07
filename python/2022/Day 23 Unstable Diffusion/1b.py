from funcitons import drawElves, find_empty_squares

data = [line.strip() for line in open("Day 23/rawData.txt")]

elf_positions = []
for row_ind, row in enumerate(data):
    for col_ind, char in enumerate(row):
        if char == "#": elf_positions.append((row_ind, col_ind))

def get_directions(pos, round):
    N = pos[0]-1, pos[1]
    S = pos[0]+1, pos[1]
    E = pos[0], pos[1]+1
    W = pos[0], pos[1]-1
    NE = pos[0]-1, pos[1]+1
    SE = pos[0]+1, pos[1]+1
    NW = pos[0]-1, pos[1]-1
    SW = pos[0]+1, pos[1]-1

    rounds = [
        [[N, E, S, W, NE, SE, NW, SW], [N, NE, NW], [S, SE, SW], [W, NW, SW], [E, NE, SE]],
        [[N, E, S, W, NE, SE, NW, SW], [S, SE, SW], [W, NW, SW], [E, NE, SE], [N, NE, NW]],
        [[N, E, S, W, NE, SE, NW, SW], [W, NW, SW], [E, NE, SE], [N, NE, NW], [S, SE, SW]],
        [[N, E, S, W, NE, SE, NW, SW], [E, NE, SE], [N, NE, NW], [S, SE, SW], [W, NW, SW]]
    ]
    
    return rounds[round % 4]


drawElves(elf_positions)

last_position = []

rounds = 0
while last_position != elf_positions:
    last_position = elf_positions.copy()
    elf_target_positions = []
    for elf in elf_positions:
        directions = get_directions(elf, rounds)
        adjacent_elf = False
        for pos in directions[0]:
            if pos in elf_positions:
                adjacent_elf = True
                break
        target_pos = elf
        if adjacent_elf:
            for side in directions[1:]:
                open = True
                for pos in side:
                    if pos in elf_positions:
                        open = False
                if open:    
                    target_pos = side[0]
                    break
        elf_target_positions.append(target_pos)


    new_elf_positions = []
    for index, target_pos in enumerate(elf_target_positions):
        temp_list = elf_target_positions.copy()
        temp_list.remove(target_pos)
        if target_pos in temp_list:
            new_elf_positions.append(elf_positions[index])
        else: new_elf_positions.append(target_pos)
    print(f"round {rounds+1}")
    elf_positions = new_elf_positions.copy()
    
    rounds += 1


print(rounds)
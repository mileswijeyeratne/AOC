data = [line.strip() for line in open("Day 17/rawData.txt")]


rocks = [
    [
        "####"
    ],

    [
        ".#.",
        "###",
        ".#."
    ],

    [
        "###",
        "..#",
        "..#"
    ],

    [
        "#",
        "#",
        "#",
        "#"
    ],

    [
        "##",
        "##"
    ]
]

rock_dimentions = [
    (4, 1),
    (3, 3),
    (3, 3),
    (1, 4),
    (2, 2)
]

current_rock_total = 0

current_stack = [
    ["#","#","#","#","#","#","#"],
    [".",".",".",".",".",".","."],
    [".",".",".",".",".",".","."],
    [".",".",".",".",".",".","."],
]
current_stack_height = 0

def get_rock_positions(rock_type, rock_topleft):
    rock_positions = []
    for row_index, line in enumerate(rocks[rock_type]):
        for col_index, spot in enumerate(line):
            if spot == "#":
                rock_positions.append((rock_topleft[0]+row_index, rock_topleft[1]+col_index))
    return rock_positions

def check_collide_wall(rock_type, rock_topleft):
    if rock_topleft[1] + rock_dimentions[rock_type][0] >= 7 or rock_topleft[1] < 0:
        return True
    return False

def check_collide_pile(rock_type, rock_topleft):
    rock_positions = get_rock_positions(rock_type, rock_topleft)
    for index, val in enumerate(current_stack[current_stack_height]):
        if val == "#" and (current_stack_height, index) in rock_positions:
            return True
    return False

def spawn_rock(current_rock_total, current_stack_height):
    rock_type = current_rock_total % 5
    current_rock_total += 1
    rock_topleft = (3, current_stack_height + 4)
    return (rock_type, rock_topleft, 0)

def place_rock(rock_type, rock_topleft):
    global current_stack
    global current_stack_height
    while rock_dimentions[rock_type][1] > 3 + len(current_stack):
        current_stack.append([".",".",".",".",".",".","."])
    rock_positions = get_rock_positions(rock_type, rock_topleft)
    for pos in rock_positions:
        print(pos)
        current_stack[pos[0]][pos[1]] = "#"
    current_stack_height += rock_dimentions[rock_type][1]

def tick_air(rock_type, rock_topleft, rock_age):
    """Returns True if collision otherwise returns the new pos"""
    if data[rock_age] == ">": direction = 1
    else: direction = -1
    pos_to_check = (rock_topleft[0], rock_topleft[1]+direction)
    if not check_collide_pile(rock_type, pos_to_check) and not check_collide_wall(rock_type, pos_to_check):
        return pos_to_check
    return rock_topleft

def tick_gravity(rock_type, rock_topleft, rock_age):
    """Returns True if collision otherwise returns the new pos"""
    rock_age += 1
    pos_to_check = (rock_topleft[0]-1, rock_topleft[1])
    if not check_collide_pile(rock_type, pos_to_check):
        return pos_to_check
    return True

last_printed = None
while current_rock_total < 2022:
    rock_type, rock_pos, rock_age = spawn_rock(current_rock_total, current_stack_height)
    new_pos = rock_pos
    while new_pos != True:
        rock_pos = new_pos
        rock_pos = tick_air(rock_type, rock_pos, rock_age)
        new_pos = tick_gravity(rock_type, rock_pos, rock_age)
    place_rock(rock_type, rock_pos)
    if current_rock_total % 10 == 0 and current_rock_total != last_printed:
        print(f"{current_rock_total:,}")
        last_printed = current_rock_total

print(current_stack_height)
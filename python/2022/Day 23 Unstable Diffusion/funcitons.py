def vectorAdd(vec1, vec2):
    return (vec1[0]+vec2[0], vec1[1] + vec2[1])

def drawElves(elfpositions):
    elves = elfpositions
    min_row, max_row, min_col, max_col = elves[0][0], elves[0][0], elves[0][1], elves[0][1]
    for elf in elves:
        if elf[0] < min_row: min_row = elf[0]
        elif elf[0] > max_row: max_row = elf[0]
        if elf[1] < min_col: min_col = elf[1]
        elif elf[1] > max_col: max_col = elf[1]
    map = []
    for row in range(min_row, max_row+1):
        map.append(["." for _ in range(min_col, max_col+5)])
    for elf in elves:
        map[elf[0]-min_row][elf[1]-min_col] = "#"
    print("")
    for row in map:
        line_to_print = ""
        for char in row: line_to_print = line_to_print + char
        print(line_to_print)
    print("")

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
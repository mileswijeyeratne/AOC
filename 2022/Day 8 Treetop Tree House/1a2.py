input = [line.strip() for line in open("Day 8/rawData.txt")]

def solve(x):
    visible_trees = []
    directions = [[0,1], [0,-1], [1,0], [-1, 0]]

    for row_index, row in enumerate(x):
        for column_index, column in enumerate(row):
            visible = True
            for direction in directions:
                if visible:
                    search_pos = [row_index, column_index]
                    while search_pos[0] > 0 and search_pos[0] < len(row)-1 and search_pos[1] > 0 and search_pos[1] < len(x)-1 and visible:
                        search_pos[0] += direction[0]
                        search_pos[1] += direction[1]
                        if input[search_pos[0]][search_pos[1]] >= column:
                            visible = False
            if visible: visible_trees.append((row_index, column_index))
    print(len(visible_trees))
    print(set(visible_trees))
    return len(set(visible_trees))

print(solve(input))
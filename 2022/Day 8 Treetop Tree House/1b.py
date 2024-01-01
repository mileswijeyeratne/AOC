input = [line.strip() for line in open("Day 8/rawData.txt")]


def solve(x):

    tree_distances = {}

    for row_index, row in enumerate(x):
        current_tree = -1
        for tree_index, tree in enumerate(row):
            if int(tree) > current_tree:
                tree_distances[(row_index, tree_index)] = tree_index
            else:
                tree_distances[(row_index, tree_index)] = 0
        current_tree = -1
        temp_row = row[::-1]
        for tree_index, tree in enumerate(temp_row):
            if int(tree) > current_tree:
                visible_trees.append((row_index, len(row)-tree_index-1))
                current_tree = int(tree)

    columns = []
    for i in range(len(input[0])):
        columns.append("")
    for row in input:
        for tree_index, tree in enumerate(row):
            columns[tree_index] = columns[tree_index] + tree
    for column_index, column in enumerate(columns):
        current_tree = -1
        for tree_index, tree in enumerate(column):
            if int(tree) > current_tree:
                visible_trees.append((tree_index, column_index))
                current_tree = int(tree)
        current_tree = -1
        temp_column = column[::-1]
        for tree_index, tree in enumerate(temp_column):
            if int(tree) > current_tree:
                visible_trees.append((len(column)-tree_index-1, column_index))
                current_tree = int(tree)

    visible_trees = set(visible_trees)
    return len(visible_trees)

    
print(solve(input))
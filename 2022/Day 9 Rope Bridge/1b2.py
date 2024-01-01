data = [line.strip().split(" ") for line in open("Day 9/rawData.txt")]
input = []
for line in data:
    for i in range(int(line[1])):
        input.append(line[0])


def solve(x):
    snake = [
        [0,0],  # Head
        [0,0],  # 1
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0]   # 9
    ]
    tail_squares = []

    def update_head(command):
        directions = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}
        snake[0][0] += directions[command][0]
        snake[0][1] += directions[command][1]
    
    def update_node(index):
        node_to_update = snake[index]
        tied_to = snake[index - 1]
        if abs(node_to_update[0]-tied_to[0]) <= 1 and abs(node_to_update[1]-tied_to[1]) <= 1:
            return
        if node_to_update[0] > tied_to[0]: node_to_update[0] -= 1
        elif node_to_update[0] < tied_to[0]: node_to_update[0] += 1
        if node_to_update[1] > tied_to[1]: node_to_update[1] -= 1
        elif node_to_update[1] < tied_to[1]: node_to_update[1] += 1
        snake[index] = node_to_update

    def draw():
        canvas = []
        for i in range(30):
            line = []
            for i in range(30):
                line.append(".")
            canvas.append(line)
        
        for i in tail_squares:
            canvas[i[0]+15][i[1]+15] = "#"
        canvas[15][15] = "S"

        output = []
        for row in canvas:
            line_to_print = ""
            for item in row:
                line_to_print = line_to_print + item
            output.append(line_to_print)

        for line in output: print(line)
        print()

    for line in x:
        update_head(line)
        for i in range(1,10):
            update_node(i)
            if i == 9 and tuple(snake[9]) not in tail_squares:
                tail_squares.append((snake[9][0], snake[9][1]))

    
    #draw()
    return len(tail_squares)

print(solve(input))
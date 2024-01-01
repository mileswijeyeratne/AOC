input = [line.strip() for line in open("Day 8/rawData.txt")]

data = []
for line in input:
    line_to_add = []
    for char in line:
        line_to_add.append(int(char))
    data.append(line)


def solve(x):
    highscore = 0
    highscore_index = None
    directions = [[0,1], [0,-1], [1,0], [-1, 0]]

    for row_index, row in enumerate(x):
        for col_index, tree in enumerate(row):
            score = []
            for direction in directions:
                search = [row_index+direction[0], col_index+direction[1]]
                distance = 0
                blocked = False
                while not blocked:
                    if search[0] < 0 or search[0] >= len(row) or search[1] < 0 or search[1] >= len(x):
                        score.append(distance)
                        blocked = True
                    elif data[search[0]][search[1]] >= tree:
                        score.append(distance+1)
                        blocked = True
                    distance += 1
                    search[0] += direction[0]
                    search[1] += direction[1]
                    
            print(score)
            total_score = 1
            for i in score:
                total_score *= i
            if total_score > highscore: 
                highscore = total_score
                highscore_index = (row_index, col_index)

    return highscore, highscore_index

print(solve(data))
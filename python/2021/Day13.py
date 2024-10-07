def _parse_data(data):
    points, instructions = data.split("\n\n")
    points = set([tuple(map(int, p.split(","))) for p in points.split("\n")])
    instructions = [i[11:].split("=") for i in instructions.split("\n")]
    instructions = [(i[0], int(i[1])) for i in instructions]
    return points, instructions

def _fold(points, instructions):
    for d, pos in instructions:
        points = set(map(
            lambda p: (pos - abs(pos - p[0]) if d == "x" else p[0], pos - abs(pos - p[1]) if d == "y" else p[1]),
            points
        ))

    return points

def solvePartA(data):
    points, instructions = _parse_data(data)

    return len(_fold(points, [instructions[0]]))

def solvePartB(data):
    points, instructions = _parse_data(data)

    points = _fold(points, instructions)

    max_x = max(points, key=lambda x: x[0])[0]
    min_x = min(points, key=lambda x: x[0])[0]
    max_y = max(points, key=lambda x: x[1])[1]
    min_y = min(points, key=lambda x: x[1])[1]

    res = [[" " for _ in range(min_x, max_x+1)] for _ in range(min_y, max_y+1)]

    for x, y in points:
        res[y+min_y][x+min_x] = "\u2588"

    return "\n".join(["".join(l) for l in res])


if __name__ == "__main__":
    test = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

    print(solvePartB(test))

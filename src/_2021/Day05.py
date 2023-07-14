def _parse_data(data):
    res = []
    for line in data.split("\n"):
        pairs = [pair.split(",") for pair in line.split(" -> ")]
        res.append(tuple([(int(pair[0]), int(pair[1])) for pair in pairs]))
    return res

def _count_points(points):
    res = 0
    for point, count in points.items():
        if count >= 2:
            res += 1
    return res

def solvePartA(data):
    data = _parse_data(data)

    points = {}

    for p1, p2 in data:
        x1, y1 = p1
        x2, y2 = p2
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                points[(x1, y)] = points.get((x1, y), 0) + 1
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                points[(x, y1)] = points.get((x, y1), 0) + 1

    return _count_points(points)


def solvePartB(data):
    data = _parse_data(data)

    points = {}

    for p1, p2 in data:
        x1, y1 = p1
        x2, y2 = p2
        x_inc = y_inc = 0
        if x1 > x2: x_inc = -1
        if x1 < x2: x_inc = 1
        if y1 > y2: y_inc = -1
        if y1 < y2: y_inc = 1

        x, y = x1, y1
        points[(x, y)] = points.get((x, y), 0) + 1
        while x != x2 or y != y2:
            x += x_inc
            y += y_inc
            points[(x, y)] = points.get((x, y), 0) + 1

    return _count_points(points)


if __name__ == "__main__":
    test = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

    print(solvePartB(test))
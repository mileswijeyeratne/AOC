def _parse_data(data):
    res = []
    for line in data.split("\n"):
        l = []
        for c in line:
            l.append(int(c))
        res.append(l)
    return res


def solvePartA(data):
    data = _parse_data(data)
    size_r = len(data)
    size_c = len(data[0])
    res = 0
    for ri, row in enumerate(data):
        for ci, cell in enumerate(row):
            minimum = True
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                rind = ri + dr
                cind = ci + dc
                if 0 <= rind < size_r and 0 <= cind < size_c:
                    if data[rind][cind] <= cell:
                        minimum = False
                        break
            res += 1 + cell if minimum else 0
    return res


def _simulate(data, r, c, size_r, size_c):
    ri = r
    ci = c
    while True:
        minimum = True
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            rind = ri + dr
            cind = ci + dc
            if 0 <= rind < size_r and 0 <= cind < size_c:
                if data[rind][cind] < data[ri][ci]:
                    minimum = False
                    ri, ci = rind, cind
                    break
        if minimum: return rind, cind


def solvePartB(data):
    data = _parse_data(data)
    areas = {}
    size_r = len(data)
    size_c = len(data[0])
    for ri, row in enumerate(data):
        for ci, cell in enumerate(row):
            if cell != 9:
                res = _simulate(data, ri, ci, size_r, size_c)
                areas[res] = areas.get(res, 0) + 1
    topthree = sorted([item for _, item in areas.items()], reverse=True)[:3]
    return topthree[0] * topthree[1] * topthree[2]


if __name__ == "__main__":
    test = """2199943210
3987894921
9856789892
8767896789
9899965678"""

    print(solvePartB(test))

def _parse_data(data):
    res = []
    for line in data.split("\n"):
        l = []
        for c in line:
            l.append(int(c))
        res.append(l)
    return data


def solvePartA(data):
    data = _parse_data(data)
    return


def solvePartB(data):
    data = _parse_data(data)
    return


if __name__ == "__main__":
    test = """2199943210
3987894921
9856789892
8767896789
9899965678"""

    print(solvePartA(test))
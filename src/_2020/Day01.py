def _parse_data(data):
    return [int(line) for line in data.split("\n")]


def solvePartA(data):
    data = _parse_data(data)

    for i, n in enumerate(data):
        for m in data[i:]:
            if n+m == 2020:
                return n*m

    return "No solution"


def solvePartB(data):
    data = _parse_data(data)

    for i, n in enumerate(data):
        for j, m in enumerate(data[i:]):
            for l in data[i+j:]:
                if l+m+n == 2020:
                    return l*m*n

    return "No solution"


if __name__ == "__main__":
    test = """1721
979
366
299
675
1456"""

    print(solvePartB(test))

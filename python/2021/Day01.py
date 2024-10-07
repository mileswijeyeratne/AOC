def _count(data):
    c = 0
    l = float("inf")
    for i in data:
        if i > l:
            c += 1
        l = i
    return c


def solvePartA(data):
    data = [int(i) for i in data.split("\n")]
    return _count(data)


def solvePartB(data):
    d = [int(i) for i in data.split("\n")]
    data = [sum(d[i:i + 3]) for i in range(len(d) - 2)]
    return _count(data)


if __name__ == "__main__":
    test = """199
200
208
210
200
207
240
269
260
263"""

    print(solvePartB(test))

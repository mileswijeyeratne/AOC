def _parse_data(data):
    return [[int(c) for c in line] for line in data.split("\n")]


def _print(data):
    for line in data: print(line)
    print("\n")


def solvePartA(data):
    data = _parse_data(data)
    flashes = 0

    size_r = len(data)
    size_c = len(data[0])

    for step in range(100):
        unchanged = False

        for ri, row in enumerate(data):
            for ci, cell in enumerate(row):
                data[ri][ci] += 1
                if cell > 8:
                    unchanged = True

        while unchanged:
            unchanged = False
            for ri in range(size_r):
                for ci in range(size_c):
                    if data[ri][ci] > 9:
                        data[ri][ci] = 0
                        flashes += 1
                        unchanged = True
                        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                            rind = ri + dr
                            cind = ci + dc
                            if 0 <= rind < size_r and 0 <= cind < size_c:
                                if data[rind][cind] != 0: data[rind][cind] += 1

    return flashes


def _check_syncronous(data):
    for row in data:
        for cell in row:
            if cell != 0: return False
    return True


def solvePartB(data):
    data = _parse_data(data)

    size_r = len(data)
    size_c = len(data[0])

    step = 0
    while True:
        step += 1
        unchanged = False

        for ri, row in enumerate(data):
            for ci, cell in enumerate(row):
                data[ri][ci] += 1
                if cell > 8:
                    unchanged = True

        while unchanged:
            unchanged = False
            for ri in range(size_r):
                for ci in range(size_c):
                    if data[ri][ci] > 9:
                        data[ri][ci] = 0
                        unchanged = True
                        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                            rind = ri + dr
                            cind = ci + dc
                            if 0 <= rind < size_r and 0 <= cind < size_c:
                                if data[rind][cind] != 0: data[rind][cind] += 1

        if _check_syncronous(data): return step


if __name__ == "__main__":
    test = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

    print(solvePartB(test))

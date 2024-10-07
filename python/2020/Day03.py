def _parse_data(data):
    return [list(r) for r in data.split("\n")]


def _count_trees(data, x_offset, y_offset):
    x = 0
    row_length = len(data[0])

    res = 0
    for row in data[::y_offset]:
        res += row[x] == "#"
        x = (x + x_offset) % row_length

    return res


def solvePartA(data):
    data = _parse_data(data)

    return _count_trees(data, 3, 1)


def solvePartB(data):
    data = _parse_data(data)

    res = 1

    for pair in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        res *= _count_trees(data, *pair)

    return res


if __name__ == "__main__":
    test = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""

    print(solvePartB(test))

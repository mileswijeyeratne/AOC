"""
https://adventofcode.com/2023/day/14
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 14   03:11:57  11905      0   14:22:38  18471      0

(Didn't get up early and only had time do do part b after school
 part b took too much time to debug - i confused myself with orientations and rotations of the grid)
"""

TESTDATA = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

def _parse_data(data):
    return data.split("\n")


def _tilt(row):
    # tilts to the left
    res = ""
    num_circle = 0
    num_empty = 0

    for cell in row[::-1]:
        if cell == "O": num_circle += 1
        elif cell == ".": num_empty += 1
        elif cell == "#":
            res += "." * num_empty
            res += "O" * num_circle
            res += "#"
            num_circle = num_empty = 0

    
    res += "." * num_empty
    res += "O" * num_circle

    return res[::-1]


def _calc_load(row):
    # counts where the left is north
    res = 0
    for i, c in enumerate(row[::-1]):
        if c == "O": res += i + 1
    return res


def A(data):
    data = _parse_data(data)
    data = ["".join([row[i] for row in data]) for i in range(len(data[0]))]

    tilted = [_tilt(row) for row in data]

    res = sum(_calc_load(row) for row in tilted)

    return res


def _print(data):
    res = ["".join([row[i] for row in data[::-1]]) for i in range(len(data[0]))]
    for row in res: print(row)
    print("")


def _cycle(data):
    for _ in range(4):
        data = [_tilt(row) for row in data]
        data = ["".join([row[i] for row in data[::-1]]) for i in range(len(data[0]))]
    return data


def hashable(data):
    return "".join(data)


def B(data):
    data = _parse_data(data)
    data = ["".join([row[i] for row in data]) for i in range(len(data[0])-1, -1, -1)]

    seen = {}

    i = 1000000000

    while i > 0:
        oveflow = False
        if (last_i:=seen.get(hashable(data))):
            repeat_period = last_i - i
            if repeat_period < i:
                i %= repeat_period
            else:
                oveflow = True
        if oveflow or (last_i is None):
            seen[hashable(data)] = i
            data = _cycle(data)
            i -= 1

    return sum(_calc_load(row) for row in data)


if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run AOC day 14")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    with open("../session.txt") as f:
        session = f.read().strip()
    input_data = TESTDATA if args.t else aocd.get_data(
        session=session,
        day=14,
        year=2023)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)
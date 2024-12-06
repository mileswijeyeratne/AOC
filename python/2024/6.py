"""
https://adventofcode.com/2024/day/6

      -------Part 1--------   -------Part 2--------
Day       Time  Rank  Score       Time  Rank  Score
  6   00:15:25  2434      0   00:27:23  1359      0

not too bad of a day yk
very naive approach for part 2 just checked every point in
part 1 solution. Ran in ~7s
"""

TESTDATA = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


def _parse_data(data):
    return data.split("\n")


def get_start(data):
    for ri, row in enumerate(data):
        for ci, c in enumerate(row):
            if c == "^":
                return ri, ci


# just simulate it
def calc(data, start, ri=-1, ci=-1, return_visited=False):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    cr, cc = start
    d = 0

    # tracks directions and location
    positions = set()
    positions.add((cr, cc, d))

    # tracks location
    visited = set()
    visited.add((cr, cc))
    while True:
        nr, nc = dirs[d][0] + cr, dirs[d][1] + cc
        if not (0 <= nr < len(data) and 0 <= nc < len(data[0])):
            break
        if data[nr][nc] == "#" or (nr == ri and nc == ci):
            d += 1
            d %= 4
        else:
            cr, cc = nr, nc
            if (cr, cc, d) in positions:
                # print_map(data, visited)
                return -1
            positions.add((cr, cc, d))
            visited.add((cr, cc))
    return len(visited) if not return_visited else visited


def print_map(data, res):
    for i in range(len(data)):
        print("".join("X" if (i, j)
              in res else data[i][j] for j in range(len(data[0]))))


def A(data):
    data = _parse_data(data)
    start = get_start(data)

    return calc(data, start)


def B(data):
    data = _parse_data(data)
    start = get_start(data)
    positions = calc(data, start, return_visited=True)

    res = 0
    # just check all positions that the original path visited
    for r, c in positions:
        if calc(data, start, r, c) == -1:
            res += 1
    return res


if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    import os
    parser = ArgumentParser(description="Run AOC day 1")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    session = os.environ.get("aoc-session")
    assert session is not None, "Please set 'aoc-session' environment variable"

    input_data = TESTDATA if args.t else aocd.get_data(
        session=session,
        day=6,
        year=2024)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)

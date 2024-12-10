"""
https://adventofcode.com/2024/day/10

      -------Part 1--------   -------Part 2--------
Day       Time  Rank  Score       Time  Rank  Score
 10   00:16:55  2383      0   00:18:56  1930      0

so annoying I couldve got it so quickly
I misread and did part 2 for part 1 by mistake and spent ages debugging
also right about now is when I wish i spent more time on grid helper functions
"""

TESTDATA = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""


def _parse_data(data):
    def m(c): return -1 if c == "." else int(c)
    return [list(map(m, line)) for line in data.split("\n")]


def dfs(data, row, col, height, ends):
    if height == 9:
        ends.add((row, col))  # part a
        return 1  # part b

    res = 0
    for dir in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        dr, dc = dir
        nextr, nextc = dr + row, dc + col
        if not (0 <= nextr < len(data) and 0 <= nextc < len(data[0])):
            continue
        if not (data[nextr][nextc] == height + 1):
            continue
        res += dfs(data, nextr, nextc, height+1, ends)

    return res


def A(data):
    data = _parse_data(data)
    res = 0
    for i, row in enumerate(data):
        for j, c in enumerate(row):
            if c == 0:
                s = set()
                dfs(data, i, j, 0, s)
                res += len(s)
    return res


def B(data):
    data = _parse_data(data)
    res = 0
    for i, row in enumerate(data):
        for j, c in enumerate(row):
            if c == 0:
                res += dfs(data, i, j, 0, set())
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
        day=10,
        year=2024)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)

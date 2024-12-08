"""
https://adventofcode.com/2024/day/8

      -------Part 1--------   -------Part 2--------
Day       Time  Rank  Score       Time  Rank  Score
  8   00:12:20  1104      0   00:23:11  1677      0

alr day ig
had quite an annoying but in part 2 that took me a couple mins
to fix. I was adding where I shouldve subtracted and swapped around
dx and dx.
"""

from collections import defaultdict
from math import gcd

TESTDATA = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""


def _parse_data(data):
    data = data.split("\n")
    res = defaultdict(set)
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if c != ".":
                res[c].add((i, j))
    return len(data), len(data[0]), res


def A(data):
    n, m, data = _parse_data(data)
    res = set()
    for freq in data:
        for p in data[freq]:
            for q in data[freq]:
                if p == q:
                    continue
                dx = p[0] - q[0]
                dy = p[1] - q[1]
                a = p[0] + dx, p[1] + dy
                b = q[0] - dx, q[1] - dy
                if (0 <= a[0] < n and 0 <= a[1] < m):
                    res.add(a)
                if (0 <= b[0] < n and 0 <= b[1] < m):
                    res.add(b)

    return len(res)


def B(data):
    n, m, data = _parse_data(data)
    res = set()
    for freq in data:
        for p in data[freq]:
            for q in data[freq]:
                if p == q:
                    continue
                dx = p[0] - q[0]
                dy = p[1] - q[1]
                g = gcd(dx, dy)
                dx //= g
                dy //= g
                a = b = p
                while (0 <= a[0] < n and 0 <= a[1] < m):
                    res.add(tuple(a))
                    a = a[0] + dx, a[1] + dy
                if (0 <= b[0] < n and 0 <= b[1] < m):
                    res.add(tuple(b))
                    b = b[0] - dx, b[1] - dy

    return len(res)


if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    import os
    parser = ArgumentParser(description="Run AOC day 1")
    parser.add_argument(
        "part", choices=["a", "b"], help="The part runs")
    parser.add_argument(
        "-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    session = os.environ.get("aoc-session")
    assert session is not None, "Please set 'aoc-session' environment variable"

    input_data = TESTDATA if args.t else aocd.get_data(
        session=session,
        day=8,
        year=2024)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)

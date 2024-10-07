"""
https://adventofcode.com/2023/day/18

      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 18   00:36:38   2034      0   01:37:46   2045      0

(Wrote a flood fill for part 1 which obviously wouldn't work for part 2 and then spent 45 mins trying to get the shoelace formula
 to work. Ended up giving up and finding a library to do it for me)
"""
from shapely.geometry import Polygon

TESTDATA = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""


def _parse_data(data):
    res = []
    for row in data.split("\n"):
        dir, count, colour = row.split(" ")
        count = int(count)
        colour = colour[2:-1]
        res.append((dir, count, colour))
    return res


directions = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0),
    "0": "R",
    "1": "D",
    "2": "L",
    "3": "U",
}


def _solve(data):
    cx, cy = 0, 0

    points = []

    for dir, count in data:
        dx, dy = directions[dir]
        cx += dx * count
        cy += dy * count

        points.append([cx, cy])

    return int(Polygon(points).buffer(0.5, join_style=2).area)

def A(data):
    data = _parse_data(data)
    data = [(dir, count) for (dir, count, _) in data]
    return _solve(data)


def B(data):
    data = _parse_data(data)
    data = [(directions[hex[-1]], int(hex[:-1], 16)) for (_, _, hex) in data]
    return _solve(data)


if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run AOC day 18")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    with open("../session.txt") as f:
        session = f.read().strip()
    input_data = TESTDATA if args.t else aocd.get_data(
        session=session,
        day=18,
        year=2023)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)
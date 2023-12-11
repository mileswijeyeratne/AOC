"""
https://adventofcode.com/2023/day/11
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 11   01:58:32  10051      0   02:01:03   8622      0

(I only got up at around 1:45:00 and started at 1:50:00)
 11   00:08:32                 00:11:03    <- Approximate times actually spent coding
"""

TESTDATA = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""


def _parse_data(data):
    return [list(line) for line in data.split("\n")]

def _find_distance(a, b, empty_rows, empty_cols, space):
    lx, ux = min(a[0],b[0]), max(a[0],b[0]), 
    dx = ux - lx + sum([space for ci in empty_cols if lx < ci < ux])
    ly, uy = min(a[1],b[1]), max(a[1],b[1]), 
    dy = uy - ly + sum([space for ri in empty_rows if ly < ri < uy])
    return dx + dy

def _solve(data, part_b=False):
    space = 999999 if part_b else 1
    empty_rows = [i for i, r in enumerate(data) if all([v=="." for v in r])]
    empty_cols = [i for i in range(len(data[0])) if all([row[i]=="." for row in data])]
    galaxy_positions = []
    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            if cell == "#": galaxy_positions.append((x,y))

    res = 0
    while galaxy_positions:
        cur = galaxy_positions.pop()
        for pos in galaxy_positions:
            res += _find_distance(cur, pos, empty_rows, empty_cols, space)

    return res

def A(data):
    return _solve(_parse_data(data), part_b=False)

def B(data):
    return _solve(_parse_data(data), part_b=True)


if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run AOC day 11")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    with open("../session.txt") as f:
        session = f.read().strip()
    input_data = TESTDATA if args.t else aocd.get_data(
        session=session,
        day=11,
        year=2023)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)
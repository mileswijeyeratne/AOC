"""
https://adventofcode.com/2024/day/12

      -------Part 1--------   -------Part 2--------
Day       Time  Rank  Score       Time  Rank  Score
 12   00:15:54  1492      0   00:54:17  1668      0

kinda fun day ig
part 1 was pretty straightforward
part 2 i spent alot of time trying to write an algorithm to follow the sides
and see when they turn but realised the corners aren't acc part of the
perimeter in p1. Realised i can just subtract the number of pairs of touching
cells in the perimeter from the total to get the number of sides. e.g.:

.ppp.
p###p
.ppp.

part 1 says the perimeter (marked p) is 8
there are 4 pairs of touching perimeters (2 on the top 2 on the bottom) so the
number of sides is 8 - 4 = 4
"""

TESTDATA = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""


def _parse_data(data):
    return data.split("\n")


def floodfill(data, row, col):
    # this is a dfs ibsr
    plant = data[row][col]
    area = set()
    area.add((row, col))
    perim = set()
    q = [(row, col)]

    while q:
        row, col = q.pop()
        for i, (dr, dc) in enumerate([(1, 0), (0, 1), (-1, 0), (0, -1)]):
            nr = row + dr
            nc = col + dc
            if not (0 <= nr < len(data) and 0 <= nc < len(data[0])):
                perim.add((nr, nc, i))
                continue
            if (nr, nc) in area:
                continue
            if data[nr][nc] == plant:
                area.add((nr, nc))
                q.append((nr, nc))
            else:
                perim.add((nr, nc, i))

    return len(area), len(perim), area, perim


def A(data):
    data = _parse_data(data)
    seen = set()
    res = 0
    for i, row in enumerate(data):
        for j, c in enumerate(row):
            if (i, j) not in seen:
                a, p, area, _ = floodfill(data, i, j)
                seen.update(area)
                res += a * p
    return res


def count_sides(perim):
    counted = set()
    res = len(perim)
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for r, c, i in perim:
        for j in [(i + 1) % 4, (i - 1) % 4]:
            n = (r + dirs[j][0], c + dirs[j][1], i)
            if n not in counted and n in perim:
                res -= 1
        counted.add((r, c, i))

    return res


def B(data):
    data = _parse_data(data)
    seen = set()
    res = 0
    for i, row in enumerate(data):
        for j, c in enumerate(row):
            if (i, j) not in seen:
                a, _, area, perim = floodfill(data, i, j)
                seen.update(area)
                p = count_sides(perim)
                res += a * p
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
        day=12,
        year=2024)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)

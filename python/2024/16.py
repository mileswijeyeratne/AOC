"""
https://adventofcode.com/2024/day/16

      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 16   06:08:13  11159      0   12:52:20  12380      0


fun little dijkstra day
didn't get up early bc i was too tired again. did p1 during break and p2 when
i got home. acc wrote some quite clean code bc there was no chance of
getting on leaderboard and i wasn't drowsy af bc it wasn't 5am for once.
"""

from heapq import heappop, heappush
from collections import defaultdict

TESTDATA = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""

TESTDATA = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""


def _parse_data(data):
    data = [list(row) for row in data.split("\n")]
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            if cell == "S":
                data[i][j] = "."
                start = i, j
            if cell == "E":
                data[i][j] = "."
                end = i, j
    return data, start, end


dirs = [
    (0, 1),
    (-1, 0),
    (0, -1),
    (1, 0),
]


def dijkstra(data, start, end, *, partA):
    """
    Treats a same position with a different direction as a differnt node
    """
    q = [(0, start, (0, 1))]
    costs = defaultdict(lambda: float("inf"))
    camefrom = defaultdict(list)

    while q:
        cost, node, dir = heappop(q)

        costs[(node, dir)] = cost

        if partA and node == end:
            return cost

        # add next
        r, c = node[0] + dir[0], node[1] + dir[1]
        if data[r][c] == "." and costs[(r, c), dir] >= cost+1:
            heappush(q, (cost+1, (r, c), dir))
            camefrom[((r, c), dir)].append((node, dir))

        # or turn
        for i in range(dirs.index(dir)-1, dirs.index(dir)+2):
            new_dir = dirs[i % 4]
            if costs[(node, new_dir)] >= cost+1000:
                heappush(q, (cost+1000, node, new_dir))
                camefrom[(node, new_dir)].append((node, dir))

    return costs, camefrom


def A(data):
    return dijkstra(*_parse_data(data), partA=True)


def cost_diff(a, b):
    # turn
    if a[0] == b[0]:
        return 1000

    # step
    if a[1] == b[1]:
        return 1

    else:
        raise ValueError("not a possible move")


def count_all_paths(end, costs, camefrom):
    """
    Works by traversing the graph backwards.
    All optimal paths are ones where the difference in recorded costs between
    each node is the same as the actual cost to get between them.
    i.e at a junction the only paths backwards that we want to traverse are the
    ones whos cost is 1 smaller (step) or 1000 smaller (turn)
    """
    seen = set()  # stops loops
    res = set()  # counts nodes irrelevant of direction
    q = [(end, d) for d in dirs]
    while q:
        n = q.pop()
        res.add(n[0])
        seen.add(n)

        for node in camefrom[n]:
            if cost_diff(node, n) == costs[n] - costs[node] \
                    and node not in seen:
                q.append(node)

    return len(res)


def B(data):
    data, start, end = _parse_data(data)

    costs, camefrom = dijkstra(data, start, end, partA=False)

    return count_all_paths(end, costs, camefrom)


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
        day=16,
        year=2024)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)

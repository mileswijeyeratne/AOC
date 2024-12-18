"""
https://adventofcode.com/2024/day/18

      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 18   00:08:00    480      0   00:22:50   1581      0

had an astar implementation lying around that didn't take long to tweak
had an off by one error for a long time on part B but thought I was way out of
the ballpark bc I didn't read the question properly so lost alot of time there.
came up with a fairly clean solution although takes around 20s for part b.
"""

from collections import defaultdict
from heapq import heappush, heappop

TESTDATA = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""


def _parse_data(data):
    return [tuple(map(int, line.split(","))) for line in data.split("\n")]


def get_next(pos, positions):
    res = []
    for dir in [
        [0, 1], [1, 0], [0, -1], [-1, 0]
    ]:
        next = pos[0] + dir[0], pos[1] + dir[1]

        if any(not (0 <= n <= N) for n in next):
            continue

        if next in positions:
            continue

        res.append(next)
    return res


def reconstruct(prev, node):
    path = set()
    path.add(node)
    while node in prev:
        node = prev[node]
        path.add(node)
    return path


def search(start, target, graph):
    prev = {}

    def h(pos):
        return abs(pos[0] - target[0]) + abs(pos[1] - target[1])

    g = defaultdict(lambda: float("inf"))
    g[start] = 0

    f = defaultdict(lambda: float("inf"))
    f[start] = h(start)

    open_set = []
    heappush(open_set, (f[start], start))

    while open_set:
        _, cur = heappop(open_set)

        if cur == target:
            return f[target], reconstruct(prev, target)

        for pos in get_next(cur, graph):
            g_tentative = g[cur] + 1
            if g_tentative < g[pos]:
                prev[pos] = cur
                g[pos] = g_tentative
                f[pos] = g_tentative + h(pos)
                heappush(open_set, (f[pos], pos))

    return -1, {}


N, M = 70, 1024  # actual data
# N, M = 6, 12  # testcases


def A(data):
    data = _parse_data(data)
    cost, path = search((0, 0), (N, N), data[:M])
    return cost


def B(data):
    data = _parse_data(data)
    i = M
    while (p := search((0, 0), (N, N), data[:i])[1]) != {}:
        while data[i] not in p:
            i += 1
        i += 1
    return "".join(c for c in str(data[i-1]) if c not in " ()")


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
        day=18,
        year=2024)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)

"""
https://adventofcode.com/2023/day/24
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 24   00:51:23   1233      0   12:10:22   4326      0

(Part 1 fairly easy with some basic maths and a bit of sympy. Part 2 required some research and the discovery of z3
 Returned to part 2 in the afternoon after immediadietly realising that I didn't have the capibilities of solving for more than 2 unknowns at 5am)
"""

import sympy as sym  # part 1 -> Runs in a few mins
from z3 import * # part 2 -> runs in around 20s (Clearly z3 alot better than sympy)

TESTDATA = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""


def _parse_data(data):
    res = []
    for line in data.split("\n"):
        pos, vel = line.strip().split("@")
        pos = list(map(int, pos.split(",")))
        vel = list(map(int, vel.split(",")))
        res.append((pos, vel))
    return res


def _will_intersect_path(hailstone1, hailstone2, lb, ub):
    (x1, y1, _), (dx1, dy1, _) = hailstone1
    (x2, y2, _), (dx2, dy2, _) = hailstone2

    t1, t2 = sym.symbols("t1,t2")
    eqx = sym.Eq(t1*dx1 + x1, t2*dx2 + x2)
    eqy = sym.Eq(t1*dy1 + y1, t2*dy2 + y2)
    res = sym.solve([eqx, eqy], (t1, t2))

    if res == []: return False

    t1 = res[t1]
    t2 = res[t2]

    if t1 < 0 or t2 < 0: return False  # in the past

    x = x1 + dx1 * t1
    y = y1 + dy1 * t1

    return lb <= x <= ub and lb <= y <= ub


def A(data):
    data = _parse_data(data)

    res = 0
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if _will_intersect_path(data[i], data[j], 200000000000000, 400000000000000):
                res += 1

    return res

def B(data):
    data = _parse_data(data)[:5]  # only need a few of the hailstones as we know a solution exists

    sol = Solver()

    times = []

    sx = Int("sx")
    sy = Int("sy")
    sz = Int("sz")
    sdx = Int("sdx")
    sdy = Int("sdy")
    sdz = Int("sdz")

    for i, ((x, y, z), (dx, dy, dz)) in enumerate(data):
        t = Int(f"t{i}")
        sol.add(sx + sdx * t == x + dx * t)
        sol.add(sy + sdy * t == y + dy * t)
        sol.add(sz + sdz * t == z + dz * t)
        times.append(t)

    sol.add(Distinct(times))

    sol.check()

    model = sol.model()
    return model[sx].as_long() + model[sy].as_long() + model[sz].as_long()


if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run AOC day 24")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    try:
        with open("../session.txt") as f:
            session = f.read().strip()
    except:
        with open("session.txt") as f:
            session = f.read().strip()
    input_data = TESTDATA if args.t else aocd.get_data(
        session=session,
        day=24,
        year=2023)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)
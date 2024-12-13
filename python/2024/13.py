"""
https://adventofcode.com/2024/day/13

      -------Part 1--------   -------Part 2--------
Day       Time  Rank  Score       Time  Rank  Score
 13   00:32:05  3533      0   00:33:28  1247      0

So annoying I spent a solid bit of time with a paper and pen trying to come up
with a nice algabraic solution only to resort to z3 and do it in a few mins.
"""

import re
from z3 import Solver, Int, unsat

TESTDATA = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""


def _parse_data(data):
    pat = re.compile(r"(\d+)")
    res = []
    for tc in data.split("\n\n"):
        ba, bb, t = tc.split("\n")
        a, b = re.findall(pat, ba)
        c, d = re.findall(pat, bb)
        t1, t2 = re.findall(pat, t)

        res.append(tuple(map(int, (a, b, c, d, t1, t2))))

    return res


def solve(a, b, c, d, t1, t2):
    # wait i just clocked how does this even work
    # this isn't garunteed minimal cost
    # ig all the test cases only had 1 solution?
    s = Solver()
    A = Int("A")
    B = Int("B")
    s.add(t1 == A*a + B*c)
    s.add(t2 == A*b + B*d)
    s.add(A >= 0)
    s.add(B >= 0)
    if s.check() == unsat:
        return 0

    model = s.model()

    A = model[A].as_long()
    B = model[B].as_long()

    return 3*A + B


def A(data):
    data = _parse_data(data)
    return sum(solve(*line) for line in data)


def B(data):
    data = _parse_data(data)
    res = 0
    extra = 10000000000000
    for a, b, c, d, t1, t2 in data:
        res += solve(a, b, c, d, t1 + extra, t2 + extra)
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
        day=13,
        year=2024)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)

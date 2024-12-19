"""
https://adventofcode.com/2024/day/19

      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 19   00:08:40   1038      0   00:08:53    512      0

Fun little dp day. Very easy
predicted what part 2 would be so my part 1 implementation covered it
had an off by 1 error in part 1 so was stuck for a couple of mins
"""

from functools import lru_cache

TESTDATA = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""


def _parse_data(data):
    available, target = data.split("\n\n")
    available = set(available.split(", "))
    target = target.split("\n")
    return available, target


def solve(available, target, *, partA):
    @lru_cache
    def count(pat):
        if pat == "":
            return 1
        res = 0
        for i in range(len(pat) + 1):
            if pat[:i] in available:
                res += count(pat[i:])
        return res

    if partA:
        return sum(count(t) > 0 for t in target)
    else:
        return sum(count(t) for t in target)


def A(data):
    return solve(*_parse_data(data), partA=True)


def B(data):
    return solve(*_parse_data(data), partA=False)


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
        day=19,
        year=2024)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)

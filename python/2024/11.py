"""
https://adventofcode.com/2024/day/11

      -------Part 1--------   -------Part 2--------
Day       Time  Rank  Score       Time  Rank  Score
 11   00:05:33   743      0   00:34:00  2764      0

damn such a slow day for p2 but atleast im getting 3-digit placments for p1
took me so long to think of the hashmap approach 5am coding is not it
once I clocked it literally took like 2 min to chage p1 code
reminds me of the scratchcard day last year
"""

from collections import defaultdict

TESTDATA = """125 17"""


def _parse_data(data):
    return list(map(int, data.split()))


def calc(data, maxdepth=25):
    # refactored for duplicated code
    res = defaultdict(int)
    for d in data:
        res[d] += 1

    for _ in range(maxdepth):
        r = defaultdict(int)
        for stone, count in res.items():
            if stone == 0:
                r[1] += count
                continue
            s = str(stone)
            if len(s) % 2 == 0:
                m = len(s) // 2
                r[int(s[:m])] += count
                r[int(s[m:])] += count
                continue
            r[stone*2024] += count
        res = r

    return sum(res.values())


def A(data):
    data = _parse_data(data)
    return calc(data, maxdepth=25)


def B(data):
    data = _parse_data(data)
    return calc(data, maxdepth=75)


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
        day=11,
        year=2024)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)

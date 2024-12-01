"""
https://adventofcode.com/2024/day/1

      -------Part 1--------   -------Part 2--------
Day       Time  Rank  Score       Time  Rank  Score
  1   00:03:59  1337      0   00:05:22   888      0

parsing took way too long ibr
"""

TESTDATA = """
3   4
4   3
2   5
1   3
3   9
3   3
"""


def _parse_data(data):
    res = []
    for line in data.split("\n"):
        if not line:
            continue
        line = line.split()
        res.append((line[0], line[-1]))
    l = [int(d[0]) for d in res]
    r = [int(d[1]) for d in res]
    return l, r


def A(data):
    l, r = _parse_data(data)
    return sum(abs(a-b) for a, b in zip(sorted(l), sorted(r)))


def B(data):
    l, r = _parse_data(data)
    return sum(i * r.count(i) for i in l)


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
        day=1,
        year=2024)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)

"""
https://adventofcode.com/2024/day/22

      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 22   08:42:17  13613      0   09:04:28  10275      0

ig ive stopped getting up early then
icl today was a reading day the amount of times I didn't read the question is
crazy. pretty straightforward day tho
part 2 lost quite a bit of time as I didn't realise the test input had changed
so was getting 24 instead of 23
"""

from collections import defaultdict

TESTDATA = """1
2
3
2024"""


def _parse_data(data):
    return list(map(int, data.split("\n")))


def evolve(n):
    n = ((n * 64) ^ n) % 16777216
    n = ((n // 32) ^ n) % 16777216
    n = ((n * 2048) ^ n) % 16777216
    return n


def A(data):
    data = _parse_data(data)

    res = 0

    for i in data:
        for _ in range(2000):
            i = evolve(i)
        res += i
    return res


def B(data):
    data = _parse_data(data)

    res = defaultdict(int)

    for i in data:
        seq = ()
        seen = set()
        for _ in range(2000):
            last = i % 10
            i = evolve(i)
            diff = i % 10 - last
            if len(seq) != 4:
                seq = seq + (diff,)
            else:
                seq = seq[1:] + (diff,)

            if len(seq) == 4 and seq not in seen:
                seen.add(seq)
                res[seq] += i % 10

    return max(res.values())


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
        day=22,
        year=2024)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)

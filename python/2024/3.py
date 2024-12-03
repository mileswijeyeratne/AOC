"""
https://adventofcode.com/2024/day/3
      -------Part 1--------   -------Part 2--------
Day       Time  Rank  Score       Time  Rank  Score
  3   00:03:41   839      0   00:11:26  1399      0

not bad part a but lost alot of time on part b working out how to or in regex.
its just `|` :facepalm:
"""
import re

# part a
# TESTDATA = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
TESTDATA = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def _parse_data(data):
    return re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data)


def A(data):
    data = _parse_data(data)
    res = 0
    for i in data:
        if i in "do()don't()":
            continue
        m1, m2 = re.findall(r"\d+", i)
        res += int(m1) * int(m2)
    return res


def B(data):
    data = _parse_data(data)
    res = 0
    on = True
    for i in data:
        if i == "do()":
            on = True
            continue
        if not on:
            continue
        if i == "don't()":
            on = False
            continue
        m1, m2 = re.findall(r"\d+", i)
        res += int(m1) * int(m2)
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
        day=3,
        year=2024)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)

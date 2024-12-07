"""
https://adventofcode.com/2024/day/7

      -------Part 1--------   -------Part 2--------
Day       Time  Rank  Score       Time  Rank  Score
  7   00:16:43  3011      0   00:18:39  2078      0

very slow part 1. Took around 5 mins when I worked out the correct way.
Spent ages trying to construct permutations and evaluate them all before
realising dfs is the way to go after I clocked that oder of operations
isn't a thing. also would've been nice to know itertools.product exited.
part 2 only took 1 minute or so as I had to implement operators rather
than just using eval with the * and + chars.
"""

from operator import mul, add


TESTDATA = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


def _parse_data(data):
    res = []
    for line in data.split("\n"):
        a, b = line.split(": ")
        res.append((int(a), list(map(int, b.split()))))
    return res


def is_possible(target, nums, ops):
    # dfs
    if len(nums) == 1:
        return target == nums[0]
    for op in ops:
        new = op(nums[0], nums[1])
        # could do this faster with indices rather
        # than constructing a whole new list
        if is_possible(target, [new] + nums[2:], ops):
            return True
    return False


def concat(a, b):
    return int(str(a) + str(b))


def A(data):
    data = _parse_data(data)
    res = 0
    for target, nums in data:
        if is_possible(target, nums, [add, mul]):
            res += target

    return res


def B(data):
    data = _parse_data(data)
    res = 0
    for target, nums in data:
        if is_possible(target, nums, [add, mul, concat]):
            res += target

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
        day=7,
        year=2024)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)

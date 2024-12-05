"""
https://adventofcode.com/2024/day/5

      -------Part 1--------   -------Part 2--------
Day       Time  Rank  Score       Time  Rank  Score
  5   00:21:47  4529      0   00:49:05  5652      0

shocker of a day ibsr
first part took me ages to realise there would be duplicate keys so i was
using a dict of int -> int and overwriting rules
second part just took a while to come up with something that worked and debug
"""

from collections import defaultdict

TESTDATA = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


def _parse_data(data):
    before = defaultdict(set)
    after = defaultdict(set)
    res = []
    r, l = data.split("\n\n")
    for line in r.split("\n"):
        a, b = map(int, line.split("|"))
        before[a].add(b)
        after[b].add(a)
    for line in l.split("\n"):
        res.append(list(map(int, line.split(","))))
    return before, after, res


def A(data):
    rules, _, lines = _parse_data(data)
    res = 0
    for line in lines:
        valid = True
        for i, x in enumerate(line):
            for j, y in enumerate(line):
                if i < j and x in rules[y]:
                    valid = False
                    break
        if valid:
            res += line[(len(line)) // 2]

    return res


def B(data):
    before, after, lines = _parse_data(data)
    res = 0
    for line in lines:
        valid = True
        for i, x in enumerate(line):
            for j, y in enumerate(line):
                if i < j and x in before[y]:
                    valid = False
                    break
        if valid:
            continue
        good = []
        i = len(line) // 2
        count = {v: len(after[v] & set(line)) for v in line}
        q = [v for v, c in count.items() if c == 0]
        while len(good) <= i:  # only need to do until the valid line is half full
            n = q.pop(0)
            good.append(n)
            for v in before[n]:
                if v not in count:
                    continue
                count[v] -= 1
                if count[v] == 0:
                    q.append(v)
        res += good[-1]

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
        day=5,
        year=2024)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)

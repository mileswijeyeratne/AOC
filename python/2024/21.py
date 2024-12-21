"""
https://adventofcode.com/2024/day/21

      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 21   01:47:59   1371      0   01:48:27    496      0

Woke up late and started around half an hour (ish) in.
Quite a fun day tbf, part 1 took a while. I spent alot of time being confused
as I thought all valid sequences would be optimal.
Part 2 just requrired me to slap a memoisation ontop of p1
"""

from functools import lru_cache

TESTDATA = """029A
980A
179A
456A
379A"""


def _parse_data(data):
    return data.split("\n")


dirs = {
    (0, 1): ">",
    (0, -1): "<",
    (-1, 0): "^",
    (1, 0): "v",
}

numeric = ["789", "456", "123", " 0A"]
directional = [" ^A", "<v>"]


def calc_pos(char, keypad):
    for r, row in enumerate(keypad):
        if char in row:
            return r, row.index(char)


def calc_seqs(start, end, invalid):
    move = end[0] - start[0], end[1] - start[1]
    horizontal = "" if move[0] == 0 else abs(
        move[0]) * dirs[(move[0] // abs(move[0]), 0)]
    vertical = "" if move[1] == 0 else abs(
        move[1]) * dirs[(0, move[1] // abs(move[1]))]
    res = []
    if start[0] != invalid[0] or end[1] != invalid[1]:
        res.append(vertical+horizontal+"A")
    if start[1] != invalid[1] or end[0] != invalid[0]:
        res.append(horizontal+vertical+"A")
    return res


@lru_cache
def dfs(seq, depth=0, *, maxdepth):
    if depth == maxdepth:
        return len(seq)
    keypad = numeric if depth == 0 else directional
    r, c = calc_pos("A", keypad)
    res = 0
    start = "A"
    for char in seq:
        r, c = calc_pos(start, keypad)
        nr, nc = calc_pos(char, keypad)
        res += min(dfs(s, depth+1, maxdepth=maxdepth)
                   for s in calc_seqs((r, c), (nr, nc),
                                      (calc_pos(" ", keypad))))
        start = char
    return res


def solve(data, depth):
    data = _parse_data(data)
    return sum(int("".join(c for c in line if c.isnumeric()))
               * dfs(line, maxdepth=depth) for line in data)


def A(data):
    return solve(data, depth=3)


def B(data):
    return solve(data, depth=26)


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
        day=21,
        year=2024)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)

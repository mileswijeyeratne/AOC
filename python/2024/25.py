"""
https://adventofcode.com/2024/day/25
"""

TESTDATA = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####"""


def _parse_data(data):
    locks = []
    keys = []

    for shem in data.split("\n\n"):
        t = locks if shem[0] == "." else keys

        lines = shem.split("\n")
        r = [0] * len(lines[0])

        for l in lines:
            for i, c in enumerate(l):
                if c == "#":
                    r[i] += 1

        t.append(r)

    return locks, keys


def A(data):
    locks, keys = _parse_data(data)

    res = 0

    for l in locks:
        for k in keys:
            res += all(s <= 7 for s in map(sum, zip(l, k)))

    return res


def B(_):
    return "There is no part B!"


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
        day=25,
        year=2024)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)

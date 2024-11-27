"""
https://adventofcode.com/2020/day/13
"""
# from math import lcm

TESTDATA = """939
7,13,x,x,59,x,31,19"""


def _parse_data(data):
    lines = data.split("\n")
    return int(lines[0]), lines[1].split(",")


def A(data):
    start, ids = _parse_data(data)
    ids = [int(i) for i in ids if i.isnumeric()]
    best_id = -1
    best_time = float("inf")
    for i in ids:
        wait = (start // i + 1) * i - start
        if wait < best_time:
            best_id = i
            best_time = wait
    return best_time * best_id


def B(data):
    start, ids = _parse_data(data)
    ids = [int(c) if c.isnumeric() else 0 for c in ids]
    t = 0
    p = 1
    for i in range(len(ids)):
        if ids[i] == 0:
            continue
        while (t+i) % ids[i] != 0:
            t += p
        # p = lcm(i, p)
        p *= ids[i]  # all the numbers are primes lol lcm is not needed
    return t


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
        year=2020)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)

"""
https://adventofcode.com/2015/day/2
"""

TESTDATA = """2x3x4"""


def _parse_data(data):
    return [map(int, row.split("x")) for row in data.split("\n")]


def A(data):
    data = _parse_data(data)
    res = 0
    for l, w, h in data:
        res += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
    return res

def B(data):
    data = _parse_data(data)
    res = 0
    for l, w, h in data:
        res += sum(sorted([l, w, h])[:2]) * 2 + l*w*h
    return res


if __name__ == "__main__":
    import aocd
    from time import time_ns
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run AOC day 2")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    input_data = TESTDATA if args.t else aocd.get_data(
        session="53616c7465645f5f6a8cadc93b9182aac8706b0eaa2c354155a2097c65ae98ce052bb1a6d2f55bc96f4b164422ad0e9fdd7b28dadeb8e47a29204fa7d603cbaf",
        day=2,
        year=2015)
    part = A if args.part == "a" else B

    time_start = time_ns()
    res = part(input_data)
    time_taken_ns = time_ns() - time_start

    print("Program finished in", time_taken_ns, "nanoseconds or", time_taken_ns / 1000, "seconds):")
    print(res)

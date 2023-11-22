"""
https://adventofcode.com/2015/day/1
"""

TESTDATA = """()())"""


def _parse_data(data):
    return data.strip("\n")


def A(data):
    return _parse_data(data).count("(") - _parse_data(data).count(")")


def B(data):
    floor = 0
    for i, c in enumerate(_parse_data(data)):
        if c == "(":
            floor += 1
        else:
            floor -= 1
        if floor < 0: return i+1
    return


if __name__ == "__main__":
    import aocd
    from time import time_ns
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run AOC day 1")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    input_data = TESTDATA if args.t else aocd.get_data(
        session="53616c7465645f5f6a8cadc93b9182aac8706b0eaa2c354155a2097c65ae98ce052bb1a6d2f55bc96f4b164422ad0e9fdd7b28dadeb8e47a29204fa7d603cbaf",
        day=1,
        year=2015)
    part = A if args.part == "a" else B

    time_start = time_ns()
    res = part(input_data)
    time_taken_ns = time_ns() - time_start

    print("Program finished in", time_taken_ns, "nanoseconds or", time_taken_ns / 1000, "seconds):")
    print(res)

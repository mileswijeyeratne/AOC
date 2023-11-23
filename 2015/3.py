"""
https://adventofcode.com/2015/day/3
"""

TESTDATA = """^v^v^v^v^v"""


def _parse_data(data):
    return data.strip(" \n")


def A(data):
    data = _parse_data(data)
    houses = {(0, 0)}
    x = y = 0
    for c in data:
        if c == "<": x -= 1
        if c == ">": x += 1
        if c == "^": y -= 1
        if c == "v": y += 1
        houses.add((x, y))
    return len(houses)


def B(data):
    data = _parse_data(data)
    houses = {(0, 0)}
    xa = ya = 0
    xb = yb = 0
    for i, c in enumerate(data):
        if i % 2:
            if c == "<": xa -= 1
            if c == ">": xa += 1
            if c == "^": ya -= 1
            if c == "v": ya += 1
            houses.add((xa, ya))
        else:
            if c == "<": xb -= 1
            if c == ">": xb += 1
            if c == "^": yb -= 1
            if c == "v": yb += 1
            houses.add((xb, yb))
    return len(houses)


if __name__ == "__main__":
    import aocd
    from time import time_ns
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run AOC day 3")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    input_data = TESTDATA if args.t else aocd.get_data(
        session="53616c7465645f5f6a8cadc93b9182aac8706b0eaa2c354155a2097c65ae98ce052bb1a6d2f55bc96f4b164422ad0e9fdd7b28dadeb8e47a29204fa7d603cbaf",
        day=3,
        year=2015)
    part = A if args.part == "a" else B

    time_start = time_ns()
    res = part(input_data)
    time_taken_ns = time_ns() - time_start

    print("Program finished in", time_taken_ns, "nanoseconds")
    print(res)

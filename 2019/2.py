"""
https://adventofcode.com/2019/day/2
"""

TESTDATA = """1,0,0,0,99"""


def _parse_data(data):
    res = [int(c) for c in data.split(",")]
    res[1] = 12
    res[2] = 2
    return res


def A(data):
    data = _parse_data(data)

    pointer = 0
    while pointer < len(data):
        op = data[pointer]
        if op == 99: return data[0]
        else:
            l,r = data[data[pointer+2]], data[data[pointer+1]]
            target = 0
            if op == 1:
                target = l+r
            elif op == 2:
                target = l*r
            else: raise ValueError
            data[data[pointer+3]] = target
            pointer += 4

    return data[0], "DIDNT HALT"


def B(data):
    data = _parse_data(data)
    return data


if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run AOC day 2")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    input_data = TESTDATA if args.t else aocd.get_data(
        session="53616c7465645f5f6a8cadc93b9182aac8706b0eaa2c354155a2097c65ae98ce052bb1a6d2f55bc96f4b164422ad0e9fdd7b28dadeb8e47a29204fa7d603cbaf",
        day=2,
        year=2019)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)
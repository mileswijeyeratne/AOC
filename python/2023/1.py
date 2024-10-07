"""
https://adventofcode.com/2023/day/1

      -------Part 1--------   -------Part 2--------
Day       Time  Rank  Score       Time  Rank  Score
  1   00:03:47  1191      0   00:10:34   404      0
"""

TESTDATA = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


def _parse_data_a(data):
    res = []
    for line in data.split("\n"):
        res.append([c for c in line if c.isnumeric()])
    return res


def A(data):
    data = _parse_data_a(data)
    res = 0
    for line in data:
        res += int(line[0] + line[-1])
    return res

def _parse_data_b(data):
    res = []
    for line in data.split("\n"):
        row = []
        for i, c in enumerate(line):
            if c.isnumeric(): row.append(c)
            for d, v in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
                if line[i:].startswith(v): row.append(str(d))
        res.append(row)
    return res

def B(data):
    data = _parse_data_b(data)
    res = 0
    for line in data:
        res += int(line[0] + line[-1])
    return res



if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run AOC day 1")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    with open("../session.txt") as f:
        session = f.read().strip()
    input_data = TESTDATA if args.t else aocd.get_data(session=session, day=1, year=2023)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)
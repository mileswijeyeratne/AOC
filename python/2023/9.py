"""
https://adventofcode.com/2023/day/9
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
  9   02:23:10  12950      0   02:28:22  12481      0

(I had a very busy day so didn't get up early)
  9   00:13:10                 00:18:22    <- Approximate times actually spent coding
"""

TESTDATA = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


def _parse_data(data):
    return [list(map(int, line.split())) for line in data.split("\n")]

def _calc_next(line):
    res = 0
    temp = line
    while not all([temp[0]==temp[i] for i in range(len(temp))]):
        res += temp[-1]
        temp = [temp[i] - temp[i-1] for i in range(1, len(temp))]
    res += temp[-1]
    return res

def A(data):
    data = _parse_data(data)
    return sum([_calc_next(line) for line in data])

def _calc_previous(line):
    differenes = []
    temp = line
    while not all([temp[0]==temp[i] for i in range(len(temp))]):
        differenes.append(temp[0])
        temp = [temp[i] - temp[i-1] for i in range(1, len(temp))]
    res = temp[0]
    for d in differenes[::-1]:
        res = d - res
    return res

def B(data):
    data = _parse_data(data)
    return sum([_calc_previous(line) for line in data])

if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run AOC day 9")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    with open("../session.txt") as f:
        session = f.read().strip()
    input_data = TESTDATA if args.t else aocd.get_data(
        session=session,
        day=9,
        year=2023)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)
"""
https://adventofcode.com/2023/day/3
      -------Part 1--------   -------Part 2--------
Day       Time  Rank  Score       Time  Rank  Score
  3   00:26:47  2571      0   00:30:44  1489      0
"""

TESTDATA = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def _parse_data(data):
    return [[c for c in row] for row in data.split("\n")]

def get_neighbours(data, ri, ci):
    for dr, dc in [(-1,-1), (-1,0), (0,-1), (1,-1), (-1,1), (1,0), (0,1), (1,1)]:
        nr, nc = ri + dr, ci + dc
        if 0 <= nr < len(data) and 0 <= nc < len(data[0]):
            yield nr, nc

def find_num(data, ri, cis):
    ci = cis
    start = None
    while start is None and ci >= 0:
        if not data[ri][ci].isnumeric():
            start = ci+1
        ci -= 1
    if start == None: start = 0
    ci = cis
    end = None
    while end is None and ci < len(data[ri]):
        if not data[ri][ci].isnumeric():
            end = ci
        ci += 1
    if end == None: end = len(data[ri])
    return start, end


def A(data):
    res = 0
    data = _parse_data(data)
    for ri, row in enumerate(data):
        for ci, cell in enumerate(row):
            if not (cell.isnumeric() or cell=="."):
                for nr, nc in get_neighbours(data, ri, ci):
                    if data[nr][nc].isnumeric():
                        start, end = find_num(data, nr, nc)
                        num = int("".join(data[nr][start:end]))
                        res += num
                        for i in range(start, end): data[nr][i] = "."
    return res


def B(data):
    res = 0
    data = _parse_data(data)
    for ri, row in enumerate(data):
        for ci, cell in enumerate(row):
            if cell == "*":
                gears = []
                for nr, nc in get_neighbours(data, ri, ci):
                    if data[nr][nc].isnumeric():
                        start, end = find_num(data, nr, nc)
                        num = int("".join(data[nr][start:end]))
                        gears.append(num)
                        for i in range(start, end): data[nr][i] = "."
                if len(gears) == 2: res += gears[0] * gears[1]
    return res


if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run AOC day 3")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    input_data = TESTDATA if args.t else aocd.get_data(
        session="53616c7465645f5f6a8cadc93b9182aac8706b0eaa2c354155a2097c65ae98ce052bb1a6d2f55bc96f4b164422ad0e9fdd7b28dadeb8e47a29204fa7d603cbaf",
        day=3,
        year=2023)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)
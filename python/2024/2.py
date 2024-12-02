"""
https://adventofcode.com/2024/day/2
      -------Part 1--------   -------Part 2--------
Day       Time  Rank  Score       Time  Rank  Score
  2   00:11:53  3649      0   00:30:00  4658      0

holy shit this was a bad day
first my internet bugs out and i cant see the problem statement for a full 5 mins
then i absoultely lose braincells coding some spaghetti ahh code
and finally i add another testcase to the data to debug then forget so wonder
    why my answer keeps giving me 1 higher for a solid 10 mins
"""

TESTDATA = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


def _parse_data(data):
    return [list(map(int, line.split())) for line in data.split("\n")]


def sign(i):
    if i == 0:
        return i
    return -1 if i < 0 else 1


def is_valid(line):
    # some shite code dont judge
    diff = line[1] - line[0]
    if not (1 <= abs(diff) <= 3):
        return False
    safe = True
    for i in range(2, len(line)):
        d = line[i] - line[i - 1]
        if not (sign(d) == sign(diff) and (1 <= abs(d) <= 3)):
            safe = False
            break
    return safe


def A(data):
    data = _parse_data(data)
    return sum(is_valid(line) for line in data)


def B(data):
    data = _parse_data(data)
    res = 0

    for line in data:
        # how am i reduced to brute forcing it o(n*m) goes crazy
        # today really was not my best performance
        for i in range(len(line)):
            if is_valid(line[:i] + line[i+1:]):
                res += 1
                break

    return res


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
        day=2,
        year=2024)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)

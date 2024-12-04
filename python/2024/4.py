"""
https://adventofcode.com/2024/day/4

      -------Part 1--------   -------Part 2--------
Day       Time  Rank  Score       Time  Rank  Score
  4   00:21:18  4386      0   00:30:31  3480      0

quite a bad day
part 1: spent alot of time trying to get a point helper class to work but
eventually realised it would be easier without
part 2: had an off by 1 renge check that meant -ve indecies were allowed
which doesn't throw an error and isn't a problem for test inpu so i took
ages to track down
"""

TESTDATA = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


def _parse_data(data):
    return data.split("\n")


def A(data):
    data = _parse_data(data)
    res = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "X":
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1),
                               (1, -1), (-1, -1), (-1, 1)]:
                    ci, cj = i, j
                    for c in "MAS":
                        ci += di
                        cj += dj
                        if not (0 <= ci < len(data) and
                                0 <= cj < len(data[0])):
                            break
                        if data[ci][cj] != c:
                            break
                    else:
                        res += 1

    return res


def B(data):
    data = _parse_data(data)
    res = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "A":
                if not 0 < i < len(data) - 1:
                    continue
                if not 0 < j < len(data[0]) - 1:
                    continue
                if sorted(data[i-1][j-1] + data[i+1][j+1]) != sorted("MS"):
                    continue
                if sorted(data[i+1][j-1] + data[i-1][j+1]) != sorted("MS"):
                    continue
                res += 1

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
        day=4,
        year=2024)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)

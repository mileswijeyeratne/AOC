"""
https://adventofcode.com/2024/day/14

      -------Part 1--------   --------Part 2--------
Day       Time  Rank  Score       Time   Rank  Score
 14   02:33:11  9330      0       >24h  28793      0

Had a show today so didn't get up early to do the problem.
Read part 1 while having breakfast and looked easy enough to do before I left
came back to part 2 after doing day 15 as I didn't get a change on day 14.
"""

TESTDATA = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""


def _parse_data(data):
    res = []
    for line in data.split("\n"):
        p, v = line.split(" ")
        p = tuple(map(int, p[2:].split(",")))
        v = tuple(map(int, v[2:].split(",")))
        res.append((p, v))
    return res


def A(data):
    X, Y = 101, 103
    T = 100
    data = _parse_data(data)
    quadrants = [0, 0, 0, 0]
    for (px, py), (vx, vy) in data:
        px = (px + vx * T) % X
        py = (py + vy * T) % Y

        if px == (X - 1) // 2:
            continue
        if py == (Y - 1) // 2:
            continue

        i = 0
        if px > X / 2:
            i += 1
        if py > Y / 2:
            i += 2
        quadrants[i] += 1

    res = 1
    for i in quadrants:
        res *= i
    return res


def B(data):
    # vertical clusters: 11, 112 -> repeats every 101 (width)
    # horizontal clusters: 65, 168 -> repeats every 103 (height)
    # x mod 101 = 11
    # x mod 103 = 65
    # found using crt and code:
    #   x = 11
    #   >>> while x % 103 != 65:
    #   ...     x += 101
    #   >>> x
    #   7687
    data = _parse_data(data)
    T = 0
    X, Y = 101, 103
    while True:
        inp = input()
        T = int(inp) if inp else T + 1

        res = [["."] * X for _ in range(Y)]

        for (px, py), (vx, vy) in data:
            x = (px + vx * T) % X
            y = (py + vy * T) % Y

            res[y][x] = "#"

        print("\n".join("".join(line) for line in res))
        print(T)

    return data


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
        day=14,
        year=2024)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)

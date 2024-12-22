"""
https://adventofcode.com/2024/day/20

      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 20       >24h  20312      0       >24h  18790      0

holy this day was rough for me
was out so late on the 19th that I couldn't get up early and never got round
to it on the 20th.
took me a few days for part b lol i just didn't know where I was going wrong.
completely overcomplicated my life as I thought that as soon as a cheat went
onto the track the cheat would be over. Wrote multiple iteratations of an
algorithm to floodfill possible end locations only going thorugh walls only to
realise the answer was alot simpler.

part 3 is from reddit:
https://www.reddit.com/r/adventofcode/comments/1hih8yx/2024_day_20_part_3_your_code_is_too_general_lets/
"""

from heapq import heappop, heappush

TESTDATA = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""


def _parse_data(data):
    data = [list(line) for line in data.split("\n")]
    for i, row in enumerate(data):
        for j, c in enumerate(row):
            if c == "S":
                start = i, j
                data[i][j] = "."
            if c == "E":
                end = i, j
                data[i][j] = "."
    return data, start, end


dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def get_costs(data, start):
    costs = {}
    q = [(0, start)]
    while q:
        cost, (r, c) = heappop(q)

        costs[(r, c)] = min(costs.get((r, c), float("inf")), cost)

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if (nr, nc) in costs or data[nr][nc] != ".":
                continue
            heappush(q, (cost+1, (nr, nc)))

    return costs


def get_cheats(costs, *, cheat_dist):
    res = 0
    for (r, c), cost in costs.items():
        for dr in range(-cheat_dist, cheat_dist+1):
            for dc in range(-cheat_dist, cheat_dist+1):
                dist = abs(dr) + abs(dc)
                if dist > cheat_dist:
                    continue
                save = cost - dist - costs.get((r+dr, c+dc), float("inf"))
                if save >= 100:
                    res += 1
    return res


def A(data):
    data, start, end = _parse_data(data)
    costs = get_costs(data, end)
    return get_cheats(costs, cheat_dist=2)


def B(data):
    data, start, end = _parse_data(data)
    costs = get_costs(data, start)
    return get_cheats(costs, cheat_dist=20)


INPUTDATA_C = """#########################################
#...#.............#.....#.....#.....#...#
###.#.###.#########.###.###.#####.###.#.#
#...#...#.#.#.....#...#...#.#.........#.#
#..##.###.#.#####.#####.#.#.#.#####.#.#.#
#.......#.....#.#.....#.#...#...#...#.#.#
#.###########.#.#.####.####.#.###########
#.#.#...#...#.....#.................#...#
#.#.#.#.#.#.###.#.#.###.#########.#####.#
#.....#...#.....#...#.........#...#.#.#.#
#####.#####.#####.#.#.#.#.#######.#.#.#.#
#.....#.........#.#.#...#...#...#.#...#.#
#.#########.#######.#####.#.##..###.###.#
#...#.......#.....#.#...#.#...#.....#...#
#.###.###########.#.###.#.#.###.#######.#
#.#.#.............#.....#.#...#...#.....#
###.#.#####.#####.#.###.#.#####.#####.###
#...#.#.........#.#...#...#...#.#.....#.#
###.###.#.#########.#####.###.#.#.#.#.#.#
#S#.#...#.#.....#.....#.........#.#.#..E#
#.#.#.#########.#.#########.#.###.#####.#
#.....#.........#...#.#...#.#.....#...#.#
###.#####..##.#.#####.#.###.#####.###.###
#.#.#...#.#.#.#.#...#...#...#.........#.#
#.#.###.###.#.#.#.#####.####.##.#.#####.#
#.#.#.#.#.#...#.........#.#...#.#.#...#.#
#.#.#.#.#.#####.###.#.#.#.###.#.###.###.#
#...#.......#...#...#.#.#.........#.#...#
#######.#####.#####.###.#.#.#####.#.###.#
#.............#.....#.#.#.#.....#.......#
###############.#####.#.#########.#.#.###
#.....#...#.#.........#.#...#...#.#.#.#.#
#.#.#.#.#.#.###.#########.###.###.#####.#
#.#.#.#.#...........#.#.............#...#
###.#.#.###.#######.#.#.#.###.###.#.#.###
#...#...#...#.#...#.#...#...#.#.#.#.#...#
###.#.#######.#.#.#.###.#####.#..##.#.###
#.#.#...#.....#.#.#.......#.#.#...#.....#
#.#.#####.###.#.#.#.#.#####.#####.###.#.#
#.....#.....#.......#.............#...#.#
#########################################"""


# saw this on reddit (link at top)
# this is just a more general case where the maze isn't a single path
# works for part 1 and 2 aswell
def C(data):
    data, start, end = _parse_data(data)
    from_start = get_costs(data, start)
    from_end = get_costs(data, end)
    without_cut = from_start[end]

    res = 0
    for (r, c), cost in from_start.items():
        for dr in range(-20, 21):
            for dc in range(-20, 21):
                dist = abs(dr) + abs(dc)
                pos = r + dr, c + dc
                if dist > 20 or pos not in from_end:
                    continue
                with_cut = cost + from_end[pos] + dist
                save = without_cut - with_cut
                if save >= 30:
                    res += 1
    return res


if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    import os
    parser = ArgumentParser(description="Run AOC day 1")
    parser.add_argument("part", choices=["a", "b", "c"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    session = os.environ.get("aoc-session")
    assert session is not None, "Please set 'aoc-session' environment variable"

    input_data = TESTDATA if args.t else aocd.get_data(
        session=session,
        day=20,
        year=2024)
    part = A if args.part == "a" else B

    if args.part == "c":
        if args.t:
            print("Note: for part c, the '-t' flag does nothing")
        input_data = INPUTDATA_C
        part = C

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)

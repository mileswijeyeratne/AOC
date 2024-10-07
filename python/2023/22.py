"""
https://adventofcode.com/2023/day/22
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 22   02:08:05   2824      0   02:38:10   2540      0

(A very slow day. Part 1 took me a long time to debug, turns out I had initialised a defaultdict with a list when it should've been a set)
"""

from collections import defaultdict

TESTDATA = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""


def _parse_data(data):
    return sorted([[list(map(int, side.split(","))) for side in line.split("~")] for line in data.split("\n")], key=lambda b: min(b[0][2], b[1][2]))

def _create_brick(a, b):
    (ax, ay, az), (bx, by, bz) = a, b

    if ax != bx: return [(x, ay, az) for x in range(min(ax, bx), max(ax, bx) + 1)]
    if ay != by: return [(ax, y, az) for y in range(min(ay, by), max(ay, by) + 1)]
    if az != bz: return [(ax, ay, z) for z in range(min(az, bz), max(az, bz) + 1)]
    else: return [(ax, ay, az)]

def drop_brick(brick, part_of):
    dropped_brick = brick
    while True:
        for x, y, z in dropped_brick:
            if z == 1 or part_of.get((x, y, z-1)) is not None:
                return dropped_brick
        for i, (x, y, z) in enumerate(dropped_brick):
            dropped_brick[i] = (x, y, z-1)

def _calc_supports(data):
    part_of = {}
    bricks = []

    for i, b in enumerate(data):
        brick = _create_brick(*b)
        brick = drop_brick(brick, part_of)
        bricks.append(brick)
        for coord in brick:
            part_of[coord] = i

    # supporting: { ind: int -> the bricks that ind supports : set }
    # supported_by: { ind: int -> the bricks that support ind: set }

    supported_by = defaultdict(set)
    supporting = {i: set() for i in range(len(bricks))}
 
    for i, brick in enumerate(bricks):
        for (x, y, z) in brick:
            above = part_of.get((x, y, z+1))
            if above not in [None, i]:
                supported_by[above].add(i)
                supporting[i].add(above)
    
    return supported_by, supporting

def A(data):
    data = _parse_data(data)
    supported_by, supporting = _calc_supports(data)

    res = 0
    for supported in supporting.values():
        if all(len(supported_by[s]) != 1 for s in supported):
            res += 1

    return res


def B(data):
    data = _parse_data(data)
    supported_by, supporting = _calc_supports(data)

    res = 0
    for s, supported in supporting.items():
        
        fallen = set([s])
        for b in supported:
            if len(supported_by[b]) == 1:
                fallen.add(b)
        
        while True:
            f = len(fallen)
            
            for b, supports in supported_by.items():
                if len(supports - fallen) == 0:
                    fallen.add(b)

            if f == len(fallen): break

        res += len(fallen) - 1  # we don't want to count the disintegrated brick

    return res


if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run AOC day 22")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    with open("../session.txt") as f:
        session = f.read().strip()
    input_data = TESTDATA if args.t else aocd.get_data(
        session=session,
        day=22,
        year=2023)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)
"""
https://adventofcode.com/2023/day/17
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 17   13:04:08  10986      0   13:08:12   9835      0

(Started at around 12:00:00
 Quite a slow day as I tried to implement A* which doesn't work as a node can be reached with the last 3 moves being different)
 17   01:04:08                 01:08:12    <- Approximate actual times
"""

from queue import PriorityQueue

TESTDATA = """111111111111
999999999991
999999999991
999999999991
999999999991"""


def _parse_data(data):
    return [[int(i) for i in row] for row in data.split("\n")]

def solve(data, min_dist, max_dist):
    # Dijkstra's algorithm
    # A star was too hard to code due to the moving in one direction rule although it would've been alot faster probably

    start = 0, 0
    end = len(data) - 1, len(data[0])-1

    visited = set()
    q = PriorityQueue()
    q.put((data[start[0]][start[1] + 1], (start[0], start[1] + 1), (0, 1), 1))
    q.put((data[start[0] + 1][start[1]], (start[0] + 1, start[1]), (1, 0), 1))

    while not q.empty():
        cost, pos, dir, dir_count = q.get()

        if pos == end and dir_count >= min_dist:
            return cost
        
        if (pos, dir, dir_count) in visited:
            continue

        visited.add((pos, dir, dir_count))

        if dir_count >= min_dist:
            for new_dir in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if new_dir == dir or (new_dir[0], new_dir[1]) == (-dir[0], -dir[1]):
                    continue
                new_pos = pos[0] + new_dir[0], pos[1] + new_dir[1]
                if not (0 <= new_pos[0] < len(data) and 0 <= new_pos[1] < len(data[0])):
                    continue
                q.put((cost + data[new_pos[0]][new_pos[1]], new_pos, new_dir, 1))

        if dir_count < max_dist:
            new_pos = pos[0] + dir[0], pos[1] + dir[1]
            if 0 <= new_pos[0] < len(data) and 0 <= new_pos[1] < len(data[0]):
                q.put((cost + data[new_pos[0]][new_pos[1]], new_pos, dir, dir_count + 1))
    
    return "No solution"


def A(data):
    data = _parse_data(data)
    return solve(data, min_dist=0, max_dist=3)


def B(data):
    data = _parse_data(data)
    return solve(data, min_dist=4, max_dist=10)


if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run AOC day 17")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    with open("../session.txt") as f:
        session = f.read().strip()
    input_data = TESTDATA if args.t else aocd.get_data(
        session=session,
        day=17,
        year=2023)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)
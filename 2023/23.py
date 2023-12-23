"""
https://adventofcode.com/2023/day/23
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 23   00:44:36   1836      0   09:02:03   4842      0

(Not very happy with my solution to part a. The problem being NP-hard forced me to write a better part b so my code for that is a lot nicer.
 I might try to adapt my part B code to work on part a in the future.)
"""

from queue import Queue
from collections import defaultdict

TESTDATA = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""


def _parse_data(data):
    return [list(row) for row in data.split("\n")]


# ------ Part A ------ # 
class Front:
    def __init__(self, pos, dir, dist):
        self.pos = pos
        self.dir = dir
        self.dist = dist

    def get_next_a(self, data, E):
        res = [(self.pos, self.dir, self.dist)]
        while len(res) == 1:
            pos, dir, dist = res.pop()
            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if (-dr, -dc) != dir:
                    nr, nc = dr + pos[0], dc + pos[1]
                    if (nr, nc) == E: return [((nr, nc), (dr, dc), dist+1)]
                    cell = data[nr][nc]
                    if cell == "#": continue
                    if cell == ">" and (dr, dc) != (0, -1): res.append(((nr, nc), (0, 1), dist+1))
                    if cell == "v" and (dr, dc) != (-1, 0): res.append(((nr, nc), (1, 0), dist+1))
                    if cell == ".": res.append(((nr, nc), (dr, dc), dist+1))
        return res


def A(data):
    data = _parse_data(data)

    S = (0, 1)
    E = (len(data)-1, len(data[0])-2)
    front = Queue()
    front.put(Front(S, (1, 0), 0))
    paths = []

    while not front.empty():
        next = front.get(0)
        n = next.get_next_a(data, E)
        for pos, dir, dist in n:
            if pos == E:
                paths.append(dist)
            else:
                front.put(Front(pos, dir, dist))
    return max(paths)
# ---- End part A ---- #

# ------ Part B ------ #
def _create_graph(data, start, end):
    edges = defaultdict(list)  # {start: [(end, wieght), (end, weight), ...]}

    # bfs to create graph
    explored = set([((-1, 1),start), (start, start)])  # cell before start outside of grid
    q = Queue()
    q.put((start, start, 0))

    while not q.empty():
        pos, last_junction, dist_since_last = q.get()
        neighbours = []
        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nr, nc = dr + pos[0], dc + pos[1]
            if data[nr][nc] != "#":
                neighbours.append((nr, nc))
        
        if len(neighbours) > 2:
            if pos != last_junction: edges[last_junction].append((pos, dist_since_last))
            last_junction = pos
            dist_since_last = 0

        for n in neighbours:
            if n == end:
                edges[last_junction].append((end, dist_since_last + 1))
            else:
                if (n, last_junction) in explored: continue
                explored.add((n, last_junction))
                q.put((n, last_junction, dist_since_last + 1))

    return edges


def B(data):
    data = _parse_data(data)
    start = 0, 1
    end = len(data) - 1, len(data[0]) - 2
    graph = _create_graph(data, start, end)

    # dfs
    stack = [(start, 0, set())]  # [ (pos, cost, explored), (pos, cost, explored), ... ]
    longest = 0

    while stack:
        pos, cost, explored = stack.pop()

        for next, added_cost in graph[pos]:
            if next == end:
                longest = max(longest ,cost + added_cost)
                continue

            if next not in explored:
                new_explored = explored.copy()
                new_explored.add(pos)
                stack.append((next, cost+added_cost, new_explored))

    return longest
# ---- End part B ---- #


if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run AOC day 23")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    try:
        with open("../session.txt") as f:
            session = f.read().strip()
    except:
        with open("session.txt") as f:
            session = f.read().strip()
    input_data = TESTDATA if args.t else aocd.get_data(
        session=session,
        day=23,
        year=2023)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)
"""
https://adventofcode.com/2023/day/21
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 21   00:14:34   1409      0       >24h   9529      0

(Part 2 was pure pain. Took about 5 attempts to get right.
 Ended up being off by around 400 and couldn't fix until > 24h later. Turns out I had and off-by-1 error in line 90 where instead of L-1 I had L)
"""

TESTDATA = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""


def _parse_data(data):
    return [list(row) for row in data.split("\n")]


def get_neighbours(data, pos):
    res = []
    for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nr, nc = dr + pos[0], dc + pos[1]
        if 0 <= nr < len(data) and 0 <= nc < len(data[0]) and data[nr][nc] != "#":
            res.append((nr, nc))
    return res


def bfs(space, start, depth=999):
    explored_odd = {}
    explored_even = {start: 0}

    frontier = [start]

    for step in range(1, depth + 1): # fix parity
        if step % 2 == 0:
            explored = explored_even
        else:
            explored = explored_odd

        new_frontier = []
        while frontier:
            pos = frontier.pop()
            for new_pos in get_neighbours(space, pos):
                if new_pos not in explored:
                    explored[new_pos] = step
                    new_frontier.append(new_pos)
        frontier = new_frontier

        if not frontier:
            break

    return explored_even, explored_odd

def A(data):
    data = _parse_data(data)
    N = len(data) // 2

    explored_even, _ = bfs(data, (N, N), 64)

    return len(explored_even)


def B(data):
    data = _parse_data(data)
    N = len(data) // 2
    L = len(data)

    def p(start, steps, parity=None):
        if parity == None: parity = steps % 2
        return len(bfs(data, start, steps)[parity])

    E, O = bfs(data, (N, N))
    E, O = len(E), len(O)

    StepsA = (3*L - 3) // 2 # L + N
    A = p((0, 0), StepsA) + p((0, L-1), StepsA) + p((L-1, 0), StepsA) + p((L-1, L-1), StepsA)

    StepsB = (L - 3) // 2 # N
    B = p((0, 0), StepsB) + p((0, L-1), StepsB) + p((L-1, 0), StepsB) + p((L-1, L-1), StepsB)

    C = p((0, N), L-1) + p((N, 0), L-1) + p((L-1, N), L-1) + p((N, L-1), L-1)

    n = 202300 # (26501365 - 65) / 131 = (target_steps - N) / L  i.e number of grid copies the search exapends by

    print(StepsA, StepsB)
    print(E, O, A, B ,C)

    return (n-1)**2*O + n**2*E + (n-1)*A + n*B + C

if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run AOC day 21")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    with open("../session.txt") as f:
        session = f.read().strip()
    input_data = TESTDATA if args.t else aocd.get_data(
        session=session,
        day=21,
        year=2023)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)
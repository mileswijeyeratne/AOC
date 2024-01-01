"""
Tried multiple failed approached before finally using wikipedia and implemeting A*
"""
from collections import defaultdict
from heapq import heappush, heappop


def _parse_data(data):
    return [list(map(int, list(line))) for line in data.split("\n")]


def _log(msg):
    if msg % 10 == 0: print(f"Searching depth {msg} nodes")


def _search_naive(cost, x, y, world, depth):
    _log(depth)
    cost += world[y][x]
    nx, ny = len(world[0]), len(world)
    if x == nx - 1 and y == ny - 1:
        return cost
    best = float("inf")
    for dx, dy in [(1, 0), (0, 1)]:
        x2 = x + dx
        y2 = y + dy
        if (0 <= x2 < nx) and (0 <= y2 < ny):
            new_cost = _search_naive(cost, x2, y2, world, depth + 1)
            if new_cost < best:
                best = new_cost
    return best


def solvePartA_naive(data):
    data = _parse_data(data)
    res = _search_naive(0, 0, 0, data, 0)
    return res

# used for A
def _get_next(node, size):
    x, y = node
    return [(x + dx, y + dy) for dx, dy in [(1, 0), (0, 1)] if x + dx < size and y + dy < size]

# simple expanding search only going down and right
def _find_cost(data):
    data[0][0] = 0
    size = len(data)

    costs = defaultdict(lambda: float("inf"))
    costs[(0, 0)] = 0

    search_queue = {(0, 0)}

    while True:
        layer = set()
        while search_queue:
            cur_node = search_queue.pop()
            for node in _get_next(cur_node, size):
                layer.add(node)
                costs[node] = min(costs[cur_node] + data[node[1]][node[0]], costs[node])
        search_queue = layer.copy()
        if search_queue == set():
            break

    return costs[(size - 1, size - 1)]

# Final solution to A
def solvePartA(data):
    data = _parse_data(data)
    return _find_cost(data)

# used for B
def _extend(data):
    new_size = len(data * 5)

    for row in data:
        r = row[:]
        for _ in range(4):
            r = [i + 1 if i != 9 else 1 for i in r]
            row.extend(r)

    r = sum(data, start=[])
    data = r[:]
    for _ in range(4):
        r = [i + 1 if i != 9 else 1 for i in r]
        data.extend(r)

    res = []
    r = []
    for i, v in enumerate(data):
        r.append(v)
        if (i + 1) % new_size == 0:
            res.append(r[:])
            r = []
    return res

# used for B
def _get_bordering(node, size):
    x, y = node
    return [(x + dx, y + dy) for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)] if
            0 <= x + dx < size and 0 <= y + dy < size]

# used for B
def _taxicab_dist(node_s, node_e):
    return abs(node_s[0] - node_e[0]) + abs(node_s[1] - node_e[1])

# prints a 2d array
def _print(data):
    for line in data:
        print(" ".join(list(map(str, line))))

# unused path reconstruction for debugging
def _reconstruct(came_from, node):
    path = [node]
    while path[-1] != (0, 0):
        path.append(came_from[path[-1]])
    return path[::-1]

# Final solution to B using A*
def solvePartB(data):
    """
    Implements A* pathfinding
    https://en.wikipedia.org/wiki/A*_search_algorithm#Pseudocode
     -> h() is "_taxicab_dist" and d() is simply the value at the cell in data
     -> instead of returning a reconstructed path we just return the value
    """
    data = _extend(_parse_data(data))

    def d(node):
        return data[node[0]][node[1]]

    size = len(data)
    start = (0, 0)
    end = (size - 1, size - 1)

    g_score = defaultdict(lambda: float("inf"))
    g_score[start] = 0

    f_score = defaultdict(lambda: float("inf"))
    f_score[start] = _taxicab_dist(start, end)

    # came_from = {}

    queue = [(0, start)]

    while queue:
        _, u = heappop(queue)
        if u == end:
            return g_score[u]  # , _reconstruct(came_from, u)

        for n in _get_bordering(u, size):
            tentative_g_score = g_score[u] + d(n)
            if tentative_g_score < g_score[n]:
                # came_from[n] = u
                g_score[n] = tentative_g_score
                f_score[n] = tentative_g_score + _taxicab_dist(n, end)
                if n not in queue:
                    heappush(queue, (f_score[n], n))
    return "No path"


if __name__ == "__main__":
    test = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

    print(solvePartB(test))

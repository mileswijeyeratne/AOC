"""
https://adventofcode.com/2023/day/10
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 10   07:51:46  22062      0   13:36:21  18289      0

(I was busy and too tired to do anything in the morning.
 I only did it when I had time to throught the day)
 10   00:15:00                 00:45:00    <- Approximate times actually spent coding
"""

TESTDATA = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""


def _parse_data(data):
    res = [list("."+line+".") for line in data.split("\n")]
    res.insert(0, ["."] * len(res[0]))
    res.append(["."] * len(res[0]))
    return res

def _get_adjacent(data, x, y):
    match data[y][x]:
        case "|": return (x,y-1), (x,y+1)
        case "-": return (x-1,y), (x+1,y)
        case "F": return (x,y+1), (x+1,y)
        case "7": return (x-1,y), (x,y+1)
        case "L": return (x,y-1), (x+1,y)
        case "J": return (x,y-1), (x-1,y)
        case ".": return ()
        case c: raise ValueError(f"Unknown case {c}")    

def _get_start(data):
    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            if cell == "S":
                return (x, y)

def _get_loop_distances(data):
    S = _get_start(data)
    distances = {S: 0}
    queue = [(S[0]+dx, S[1]+dy) for (dx, dy) in [(-1, 0), (0, 1), (1, 0), (0, -1)] if S in _get_adjacent(data, S[0]+dx, S[1]+dy)]
    for item in queue: distances[item] = 1

    while queue:
        cur = queue.pop(0)
        for node in _get_adjacent(data, *cur):
            if node not in distances.keys():
                distances[node] = distances[cur] + 1
                queue.append(node)
    
    return distances

def _get_loop(data):
    S = _get_start(data)
    loop = {S}
    queue = [(S[0]+dx, S[1]+dy) for (dx, dy) in [(-1, 0), (0, 1), (1, 0), (0, -1)] if S in _get_adjacent(data, S[0]+dx, S[1]+dy)]
    for item in queue: loop.add(item)

    while queue:
        cur = queue.pop(0)
        for node in _get_adjacent(data, *cur):
            if node not in loop:
                queue.append(node)
                loop.add(node)
    
    return loop

def A(data):
    distances = _get_loop_distances(_parse_data(data))
    return max(distances.items(), key=lambda x: x[1])

def B(data):
    data = _parse_data(data)
    loop = _get_loop(data)

    # replace start with correct char
    sx, sy = _get_start(data)
    if (sy+1,sx) in loop and (sy-1,sx) in loop:
        data[sy][sx] = "|"
    elif (sy+1,sx) in loop and (sy,sx+1) in loop:
        data[sy][sx] = "F"
    elif (sy+1,sx) in loop and (sy,sx-1) in loop:
        data[sy][sx] = "7"
    elif (sy-1,sx) in loop and (sy,sx+1) in loop:
        data[sy][sx] = "L"
    elif (sy-1,sx) in loop and (sy,sx-1) in loop:
        data[sy][sx] = "J"
    elif (sy,sx+1) in loop and (sy,sx-1) in loop:
        data[sy][sx] = "-"
    res = 0

    for y in range(len(data)):
        inside = False
        last = ""
        for x in range(len(data[0])):
            if (x, y) in loop:
                cell = data[y][x]
                if cell == "|": inside = not inside
                elif cell in ["F", "L"]: last = cell
                elif cell == "J":
                    inside = inside if last == "L" else not inside
                elif cell == "7":
                    inside = inside if last == "F" else not inside
            else:
                if inside:
                    res += 1
                
    return res


if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run AOC day 10")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    with open("../session.txt") as f:
        session = f.read().strip()
    input_data = TESTDATA if args.t else aocd.get_data(
        session=session,
        day=10,
        year=2023)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)
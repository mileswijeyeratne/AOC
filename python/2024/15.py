"""
https://adventofcode.com/2024/day/15

      -------Part 1--------   -------Part 2--------
Day       Time  Rank  Score       Time  Rank  Score
 15   00:20:10   963      0   00:57:09   970      0

Holy shit this is some of the most disgusting code ive ever written
i'm acc so tired today i can't think straight
but 3 digit placement again not the worst
"""

TESTDATA = """#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^"""

TESTDATA = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""


def _parse_data(data):
    map, moves = data.split("\n\n")
    map = [list(row) for row in map.split("\n")]
    moves = moves.replace("\n", "")
    for ri, row in enumerate(map):
        for ci, cell in enumerate(row):
            if cell == "@":
                map[ri][ci] = "."
                return map, moves, (ri, ci)


dirs = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0),
    "v": (1, 0),
}


def sum_coords(map, char="O"):
    res = 0
    for i, row in enumerate(map):
        for j, c in enumerate(row):
            if c == char:
                res += 100 * i + j
    return res


def A(data):
    map, moves, (ri, ci) = _parse_data(data)

    for move in moves:
        dr, dc = dirs[move]
        nr, nc = ri + dr, ci + dc

        if map[nr][nc] == ".":
            ri, ci = nr, nc
            continue

        if map[nr][nc] == "O":
            i = 1
            while (c := map[nr + i * dr][nc + i * dc]) == "O":
                i += 1
            if c == ".":
                map[nr + i * dr][nc + i * dc] = "O"
                map[nr][nc] = "."
                ri, ci = nr, nc

    return sum_coords(map)


def printmap(map, ri, ci):
    # for debugging
    map[ri][ci] = "@"
    print("\n".join("".join(line) for line in map))
    map[ri][ci] = "."


def deepcopy(map):
    return [line.copy() for line in map]


def B(data):
    # what the acutal fuck is this function
    # even my linter is screaming at me for 'cyclomatic complexity too high'
    map, moves, (ri, ci) = _parse_data(data)

    # expand
    map = [list("".join("[]" if c == "O" else c*2 for c in row))
           for row in map]
    ci *= 2

    for move in moves:
        dr, dc = dirs[move]
        nr, nc = ri + dr, ci + dc

        if map[nr][nc] == ".":
            ri, ci = nr, nc

        elif map[nr][nc] in "[]":
            # horizontal
            if dr == 0:
                i = 1
                while (c := map[nr + i * dr][nc + i * dc]) in "[]":
                    i += 1
                if c == ".":
                    for j in range(i, -1, -1):
                        map[nr + j * dr][nc + j * dc] = map[nr +
                                                            (j-1) * dr][nc + (j-1) * dc]
                    ri, ci = nr, nc

            # move verical
            else:
                # weve got a whole ass flippin bfs here like wth
                to_move = set()
                q = [(nr, nc), (nr, nc + (1 if map[nr][nc] == "[" else -1))]
                can_move = True
                while q:
                    i, j = q.pop()
                    to_move.add((i, j))
                    i, j = i + dr, j + dc
                    if map[i][j] == ".":
                        continue
                    elif map[i][j] == "#":
                        can_move = False
                        break
                    elif (c := map[i][j]) in "[]":
                        q.append((i, j))
                        if c == "[":
                            q.append((i, j+1))
                        else:
                            q.append((i, j-1))

                if not can_move:
                    continue

                new_map = deepcopy(map)
                for i, j in to_move:
                    new_map[i+dr][j+dc] = map[i][j]
                    if (i-dr, j-dc) not in to_move:
                        new_map[i][j] = "."
                map = new_map

                ri, ci = nr, nc

    return sum_coords(map, "[")


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
        day=15,
        year=2024)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)

"""
https://adventofcode.com/2023/day/16
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 16   05:10:04  10475      0   05:19:40   9709      0

(Got up at around 4:30:00)
 16   00:40:04                 00:49:40    <- Approximate actual times
"""

from collections import defaultdict

TESTDATA = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""

def _parse_data(data):
    res = ["#" + line + "#" for line in data.split("\n")]
    return ["#"*len(res[0])] + res + ["#"*len(res[0])] 

# used for debugging
COUNT = 0

class Beam:
    def __init__(self, pos, dir):
        self.pos = pos
        self.dir = dir
        self.i = COUNT
    
    def move(self):
        self.pos = (self.pos[0] + self.dir[0], self.pos[1] + self.dir[1])
    
    def interact(self, cell):
        if cell == "-":
            if abs(self.dir[0]) == 1:
                return
            else:
                self.dir = (-1, 0)
                return Beam(self.pos, (1, 0)) 
        elif cell == "|":
            if abs(self.dir[1]) == 1:
                return
            else:
                self.dir = (0, -1)
                return Beam(self.pos, (0, 1))
        elif cell == "/":
            self.dir = (-self.dir[1], -self.dir[0])
            return
        elif cell == "\\":
            self.dir = (self.dir[1], self.dir[0])
            return
        elif cell == "#":
            return -1
        elif cell == ".":
            return
        else:
            raise ValueError(f"Invalid char: '{cell}'")
    
    def __repr__(self):
        return f"<Beam {self.i}, pos:{self.pos}, dir:{self.dir}>"

def get_energised(data, start_beam):
    beams = [
        start_beam
    ]

    # used for debugging
    global COUNT
    COUNT = 1

    activated = set()
    beam_states = defaultdict(set)

    b = beams[0]
    new_beam = b.interact(data[b.pos[1]][b.pos[0]])
    if new_beam is not None:
        beams.append(new_beam)
        COUNT += 1

    while beams:
        to_delete = []

        for i in range(len(beams)):
            b = beams[i]

            if b.dir in beam_states[b.pos]:
                to_delete.append(i)
                continue

            activated.add(b.pos)
            beam_states[b.pos].add(b.dir)
            b.move()
            new_beam = b.interact(data[b.pos[1]][b.pos[0]])
            if new_beam == -1:
                to_delete.append(i)
            elif new_beam is not None:
                beams.append(new_beam)
                COUNT += 1

        deleted = 0
        for i in to_delete:
            beams.pop(i - deleted)
            deleted += 1

    return activated

def A(data):
    data = _parse_data(data)

    activated = get_energised(data, Beam((1,1), (1, 0)))

    # dbg = [["."]*(len(data[0])-2) for _ in range(len(data[0]))]
    # for c, r in activated:
    #     dbg[r-1][c-1] = "#"
    # for r in dbg: print("".join(r))

    return len(activated)


def B(data):
    data = _parse_data(data)

    size_x = len(data[0]) - 2
    size_y = len(data) - 2

    best = set()

    # top
    for i in range(size_x):
        a = get_energised(data, Beam((i+1, 1), (0, 1)))
        if len(a) > len(best): best = a
    
    # bottom
    for i in range(size_x):
        a = get_energised(data, Beam((i+1, size_y), (0, -1)))
        if len(a) > len(best): best = a

    # left
    for i in range(size_y):
        a = get_energised(data, Beam((1, i+1), (1, 0)))
        if len(a) > len(best): best = a
    
    # bottom
    for i in range(size_y):
        a = get_energised(data, Beam((size_x, i+1), (-1, 0)))
        if len(a) > len(best): best = a

    # dbg = [["."]*(len(data[0])-2) for _ in range(len(data[0]))]
    # for c, r in best:
    #     dbg[r-1][c-1] = "#"
    # for r in dbg: print("".join(r))

    return len(best)


if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run AOC day 16")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    with open("../session.txt") as f:
        session = f.read().strip()
    input_data = TESTDATA if args.t else aocd.get_data(
        session=session,
        day=16,
        year=2023)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)
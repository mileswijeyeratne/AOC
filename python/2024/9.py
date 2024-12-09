"""
https://adventofcode.com/2024/day/9

      -------Part 1--------   -------Part 2--------
Day       Time  Rank  Score       Time  Rank  Score
  9   00:11:07   546      0   00:31:26   718      0

really not pleased with my code but placed alot better so we take these
icl i just couldn't come up with a clean solution at 5am so my code is garbage
runs pretty slow too like 5s for part a and 15s for part b
"""

TESTDATA = """2333133121414131402"""


def _parse_data(data):
    return data


def checksum(s):
    # whyd i even write a function for this when the rest of my code is so ass
    res = 0
    for i, s in enumerate(s):
        res += i * s
    return res


def A(data):
    data = _parse_data(data)
    filesystem = []
    id = 0
    for i, c in enumerate(data):
        c = int(c)
        if i % 2 == 0:
            filesystem.extend([id] * c)
            id += 1
        else:
            filesystem.extend([-1] * c)

    try:
        while True:
            i = filesystem.index(-1)
            filesystem[i], filesystem[-1] = filesystem[-1], filesystem[i]
            while filesystem[-1] == -1:
                filesystem.pop()
    except ValueError:
        pass

    return checksum(filesystem)


def B(data):
    data = _parse_data(data)
    filesystem = []
    id = 0
    for i, c in enumerate(data):
        c = int(c)
        if i % 2 == 0:
            filesystem.append((id, c))
            id += 1
        else:
            filesystem.append((-1, c))

    def index(iterable):
        for i, v in enumerate(iterable):
            if v:
                return i
        raise ValueError

    for i in range(id-1, -1, -1):
        # file to move
        file_ind = index(n[0] == i for n in filesystem)
        file = filesystem[file_ind]

        # get free space
        try:
            space_ind = index(n[0] == -1 and n[1] >= file[1]
                              for n in filesystem)
        except ValueError:
            continue

        # check space is before file
        if space_ind > file_ind:
            continue

        # move it
        space = filesystem[space_ind]
        filesystem[file_ind] = (-1, file[1])
        filesystem[space_ind] = file
        filesystem.insert(space_ind + 1, (-1, space[1] - file[1]))

    # reconstruct into format that checksum() works on
    res = []
    for i, n in filesystem:
        res.extend(max(0, i) for j in range(n))

    return checksum(res)


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
        day=9,
        year=2024)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)

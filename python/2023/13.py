"""
https://adventofcode.com/2023/day/13
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 13   00:27:19   1871      0   01:24:57   3907      0

(Windows updated when I woke up so only started at like 00:10:00 lmao)
"""

TESTDATA = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""


def _parse_data(data):
    return [chunk.split("\n") for chunk in data.split("\n\n")]

def _count_different(above, below):
    return sum([1 for (a, b) in zip(above, below) if a != b])

def _get_reflection(chunk):
    # row
    i = 1
    while i < len(chunk):
        above, below = i-1, i
        while above >= 0 and below < len(chunk):
            c =  _count_different(chunk[above], chunk[below])
            if c != 0:
                break
            above, below = above-1, below+1
        else:
            print(i)
            return i * 100
        i += 1

    # col
    rotated_chunk = ["".join([row[i] for row in chunk]) for i in range(len(chunk[0]))]
    i = 1
    while i < len(rotated_chunk):
        above, below = i-1, i
        while above >= 0 and below < len(rotated_chunk):
            c =  _count_different(rotated_chunk[above], rotated_chunk[below])
            if c != 0:
                break
            above, below = above-1, below+1
        else:
            return i
        i += 1

def _get_reflection_smudged(chunk):
    # row
    i = 1
    while i < len(chunk):
        num_diff = 0
        above, below = i-1, i
        while above >= 0 and below < len(chunk):
            c =  _count_different(chunk[above], chunk[below])
            num_diff += c
            above, below = above-1, below+1
        if num_diff == 1:
            return i * 100
        i += 1

    # col
    rotated_chunk = ["".join([row[i] for row in chunk]) for i in range(len(chunk[0]))]
    i = 1
    while i < len(rotated_chunk):
        num_diff = 0
        above, below = i-1, i
        while above >= 0 and below < len(rotated_chunk):
            c =  _count_different(rotated_chunk[above], rotated_chunk[below])
            num_diff += c
            above, below = above-1, below+1
        if num_diff == 1:
                return i
        i += 1
    return 0

def A(data):
    data = _parse_data(data)

    res = 0
    for chunk in data:
        res += _get_reflection(chunk)

    return res

def B(data):
    data = _parse_data(data)

    res = 0
    for chunk in data:
        res += _get_reflection_smudged(chunk)

    return res


if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run AOC day 13")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    with open("../session.txt") as f:
        session = f.read().strip()
    input_data = TESTDATA if args.t else aocd.get_data(
        session=session,
        day=13,
        year=2023)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)
"""
https://adventofcode.com/2023/day/12
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 12   02:19:27   7517      0   02:26:02   2658      0

(Coded my first try in 20 mins that worked on test but not full input then ended up spending 2 more hours debugging and rewriting lmao)
"""

from functools import lru_cache

TESTDATA = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

def _parse_data(data):
    res = [line.split(" ") for line in data.split("\n")]
    return [(line[0], [int(c) for c in line[1].split(",")]) for line in res]

def _get_possiblities_old(row):
    layout, known = row
    if len(known) == 0:
        return 1 if layout.count("#") == 0 else 0
    elif len(layout) == 0 or layout[0] == "#" or known[0] > len(layout) - 1:
        return 0
    else:
        res = 0
        k = known.pop(0)
        for i in range(1, len(layout)-k+1):
            if all(c in "#?" for c in layout[i:i+k]) and layout[i-1] in ".?":
                res += _get_possiblities_old((layout[i+k:], known.copy()))
            elif layout[i] == "#":
                break
        return res

def _get_possiblities(row):
    layout, known = row

    @lru_cache
    def _recurse(li, ki):
        res = 0

        if li >= len(layout): return ki == len(known) # run out of space
        if layout[li] in ".?": res += _recurse(li+1, ki) # new slice can start
        if ki == len(known): return res  # run out of slices

        k = known[ki]
        if k + li > len(layout): return res
        if all(c in "?#" for c in layout[li: li+k]) and layout[li+k] != "#":
            return res + _recurse(li+k+1, ki+1)

        return res

    return _recurse(0, 0)

def A(data):
    data = _parse_data(data)
    return sum(_get_possiblities((row[0]+".", row[1])) for row in data)

def B(data):
    data = _parse_data(data)
    data = [("?".join([row[0]]*5), row[1]*5) for row in data]
    return sum(_get_possiblities((row[0]+".", row[1])) for row in data)

if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run AOC day 12")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    with open("../session.txt") as f:
        session = f.read().strip()
    input_data = TESTDATA if args.t else aocd.get_data(
        session=session,
        day=12,
        year=2023)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)
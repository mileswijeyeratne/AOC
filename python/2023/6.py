"""
https://adventofcode.com/2023/day/6
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
  6   02:06:14  17673      0   02:10:26  16817      0  

(I started at exactly 2:00:00 becuase I didn't want to get up at 5:00am again)
  6   00:06:14                 00:10:26    <- Real times
"""

TESTDATA = """Time:      7  15   30
Distance:  9  40  200"""


def _parse_data(data):
    times, distances = data.split("\n")
    times = list(times.split()[1:])
    distances = list(distances.split()[1:])
    return times, distances


def A(data):
    times, distances = _parse_data(data)
    times = [int(c) for c in times]
    distances = [int(c) for c in distances]
    res = 1
    for i in range(len(times)):
        count = 0
        t, d = times[i], distances[i]
        for charge_time in range(1, t):
            dist_travelled = (t - charge_time) * charge_time
            if dist_travelled > d: count += 1
        res *= count
    return res


def B(data):
    time, dist = _parse_data(data)
    time, dist = int("".join(time)), int("".join(dist))
    res = 0
    for charge_time in range(1, time):
        dist_travelled = (time - charge_time) * charge_time
        if dist_travelled > dist: res += 1
    return res

if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run AOC day 6")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    with open("../session.txt") as f:
        session = f.read().strip()
    input_data = TESTDATA if args.t else aocd.get_data(
        session=session,
        day=6,
        year=2023)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)
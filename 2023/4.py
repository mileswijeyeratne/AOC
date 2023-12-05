"""
https://adventofcode.com/2023/day/4
      -------Part 1--------   -------Part 2--------
Day       Time  Rank  Score       Time  Rank  Score
  4   00:09:46  3039      0   00:43:03  6818      0
"""

TESTDATA = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def _parse_data(data):
    res = [line[5:].split(": ") for line in data.replace("  ", " ").split("\n")]
    res = {int(num): [list(map(int, side.split(" "))) for side in game.split(" | ")] for num, game in res}
    return res

def A(data):
    data = _parse_data(data)
    res = 0
    for game, line in data.items():
        count = 0
        winning, yours = line
        for num in winning:
            if num in yours:
                count += 1
        if count: res += 2**(count-1)
    return res

def B(data):
    data = _parse_data(data)
    # known = {}
    queue = {n+1: 1 for n in range(len(data))}
    res = 0
    for game in range(1, len(data)+1):
        line = data[game]
        num_cards = queue[game]
    # if game in known.keys():
    #     print("using cache on", game)
    #     numbers = known[game]
    #     for n in numbers: queue[n] = queue.get(n) + num_cards
    # else:
        count = game + 1
        winning, yours = line
        for num in winning:
            if num in yours:
                count += 1
        for n in range(game+1, count): queue[n] = queue.get(n) + num_cards
        # known[game] = list(range(game+1, count))
        res += num_cards
    return res


if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run AOC day 4")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    with open("../session.txt") as f:
        session = f.read().strip()
    input_data = TESTDATA if args.t else aocd.get_data(session=session, day=4, year=2023)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)
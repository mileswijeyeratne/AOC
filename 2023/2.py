"""
https://adventofcode.com/2023/day/2
      -------Part 1--------   -------Part 2--------
Day       Time  Rank  Score       Time  Rank  Score
  2   00:10:06  1290      0   00:12:46  1044      0
"""

TESTDATA = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


def _parse_data(data):
    res = []
    for row in data.split("\nGame "):
        t = row.split(": ")[1].split("; ")
        res.append([c.split(", ") for c in t])
    return res


def A(data):
    data = _parse_data(data)
    res = 0
    for ind, row in enumerate(data):
        is_possible = True
        for game in row:
            for colour in game:
                i, c = colour.lstrip(" ").split(" ")
                if c == "red":
                    if int(i) > 12: is_possible = False
                if c == "green":
                    if int(i) > 13: is_possible = False
                if c == "blue":
                    if int(i) > 14: is_possible = False
        if is_possible:
            res += ind + 1
            
    return res


def B(data):
    data = _parse_data(data)
    res = 0
    for ind, row in enumerate(data):
        red = green = blue = 0
        for game in row:
            for colour in game:
                i, c = colour.lstrip(" ").split(" ")
                if c == "red":
                    red = max(red, int(i))
                if c == "green":
                    green = max(green, int(i))
                if c == "blue":
                    blue = max(blue, int(i))
        res += red*green*blue
    return res


if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run AOC day 2")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    input_data = TESTDATA if args.t else aocd.get_data(
        session="53616c7465645f5f6a8cadc93b9182aac8706b0eaa2c354155a2097c65ae98ce052bb1a6d2f55bc96f4b164422ad0e9fdd7b28dadeb8e47a29204fa7d603cbaf",
        day=2,
        year=2023)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)
"""
https://adventofcode.com/2015/day/5
"""

TESTDATA = """qjhvhtzxzqqjkmpb
xxyxx
uurcxstgmygtbstg
ieodomkazucvgmuy"""


def _parse_data(data):
    return data.split("\n")


def A(data):
    data = _parse_data(data)
    nice = 0
    for word in data:
        if sum([word.count(c) for c in "aeiou"]) < 3:
            continue
        contains_double = False
        for i in range(len(word)-1):
            if word[i] == word[i+1]:
                contains_double = True
                break
        if not contains_double:
            continue
        contains_pairs = False
        for pair in ["ab", "cd", "pq", "xy"]:
            if pair in word:
                contains_pairs = True
                break
        if contains_pairs:
            continue
        nice += 1
    return nice


def B(data):
    data = _parse_data(data)
    nice = 0
    for word in data:
        between = False
        for i in range(len(word)-2):
            if word[i] == word[i+2]:
                between = True
                break
        if not between: continue

        double_pair = False
        for i in range(len(word)-3):
            if word.count(word[i:i+2]) >= 2:
                double_pair = True
        if not double_pair: continue

        nice += 1
    return nice


if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run AOC day 5")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    input_data = TESTDATA if args.t else aocd.get_data(
        session="53616c7465645f5f6a8cadc93b9182aac8706b0eaa2c354155a2097c65ae98ce052bb1a6d2f55bc96f4b164422ad0e9fdd7b28dadeb8e47a29204fa7d603cbaf",
        day=5,
        year=2015)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print("Program finished in", time_taken, "seconds")
    print(res)

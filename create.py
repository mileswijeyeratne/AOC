TEMPLATE = '''"""
https://adventofcode.com/{year}/day/{day}
"""

TESTDATA = """Test"""


def _parse_data(data):
    return data


def A(data):
    data = _parse_data(data)
    return data


def B(data):
    data = _parse_data(data)
    return data


if __name__ == "__main__":
    import aocd
    from time import time_ns
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run AOC day {day}")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    input_data = TESTDATA if args.t else aocd.get_data(
        session="{session}",
        day={day},
        year={year})
    part = A if args.part == "a" else B

    time_start = time_ns()
    res = part(input_data)
    time_taken_ns = time_ns() - time_start

    print("Program finished in", time_taken_ns, "nanoseconds or", time_taken_ns / 1000, "seconds):")
    print(res)'''

with open("session.txt") as f:
    SESSION = f.read().strip("\n")

if __name__ == "__main__":
    from argparse import ArgumentParser
    from pathlib import Path
    parser = ArgumentParser(description="Create day")
    parser.add_argument("year", type=str, help="The year of the challenge")
    parser.add_argument("day", choices=[str(i) for i in range(26)])
    args = parser.parse_args()

    root = Path(__file__).parent

    year = root / args.year
    year.mkdir(exist_ok=True)

    file = year / (args.day + ".py")
    if file.exists():
        raise Exception("File already exists")
    with file.open("w") as f:
        f.write(TEMPLATE.format(day=args.day, year=args.year, session=SESSION))

    print(f"Created day {args.day}, year {args.year}")


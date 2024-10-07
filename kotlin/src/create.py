TEMPLATE = """package y{year}

import Day

class Day{day}: Day<Day{day}.ParsedInput>({year}, {day_int}) {{
    data class ParsedInput(val a: Int)

    override fun parse(line: String): ParsedInput {{
        TODO("Not yet implemented")
    }}

    override fun part1(inp: List<ParsedInput>): Any {{
        return "Part 1 is not implemented"
    }}

    override fun part2(inp: List<ParsedInput>): Any {{
        return "Part 2 is not implemented"
    }}
}}
"""

if __name__ == "__main__":
    from argparse import ArgumentParser
    from pathlib import Path
    parser = ArgumentParser(description="Create day")
    parser.add_argument("year", type=str, help="The year of the challenge")
    parser.add_argument("day", choices=[str(i) for i in range(26)])
    args = parser.parse_args()

    root = Path(__file__).parent

    year = root / f"y{args.year}"
    year.mkdir(exist_ok=True)

    file = year / f"Day{str(args.day).zfill(2)}.kt"
    if file.exists():
        raise Exception("File already exists")
    with file.open("w") as f:
        f.write(TEMPLATE.format(day=str(args.day).zfill(2), year=args.year, day_int=args.day))

    print(f"Created day {args.day}, year {args.year}")
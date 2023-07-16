from __future__ import annotations
from pathlib import Path
from aocd import get_data
from solutions import Solution


def get_existing():
    fp = Path("data/solution_list.txt")
    with fp.open("r") as f:
        existing = f.read().split("\n")[:-1]
    solutions = [d.split("/") for d in sorted(existing)]
    existing_years = set()
    for year, _ in solutions:
        existing_years.add(year)
    return solutions, sorted(list(existing_years))


def check_exists(year, day):
    return [year, day] in get_existing()[0]


def day_to_str(day: int):
    return ("0" if day < 10 else "") + str(day)


def create_year(year: int):
    year = str(year)

    module_path = Path(f"_{year}")
    init_file_path = module_path / f"__init__.py"

    print(f"Year {year} does not have a directory - creating '_{year}' directory")
    module_path.mkdir()
    init_file_path.open("w").close()


def create_day(year: int, day: int):
    year = str(year)
    day = day_to_str(day)

    existing_solutions, existing_years = get_existing()

    module_path = Path(f"_{year}")
    solution_file_path = module_path / f"Day{day}.py"

    if [year, day] in existing_solutions:
        print("Already exists")
        return
    else:
        print(f"Creating Year {year}, Day {day}")

        if not module_path.is_dir():
            print(f"Year {year} directory does not exist - creating directory '_{year}'")
            create_year(int(year))

        # create file
        fp = Path("data/solution_template.txt")
        with fp.open("r") as f:
            template = f.read()
        with solution_file_path.open("w") as f:
            f.writelines(template)

        # redo __init__ file
        fp = module_path / "__init__.py"
        with fp.open("r+") as f:
            lines = set(f.readlines())
            lines.add(f"from . import Day{day}\n")
            f.seek(0)
            f.truncate(0)
            f.writelines(sorted(list(lines)))

        # redo solutions.py file
        fp = Path("data/solution_list_template.txt")
        with fp.open("r") as f:
            template = f.readlines()
        fp = Path("solutions.py")
        # add to _solutions dict
        template.pop(3)
        for y in existing_years[::-1]:
            days = [day for year, day in existing_solutions if year == y] + [day]
            template.insert(3, "    ],\n")  # 4 spaces instead of tab ("    " instead of "\t")
            for d in days[::-1]:
                template.insert(3, f"        (_{y}.Day{d}.solvePartA, _{y}.Day{d}.solvePartB),\n")
            template.insert(3, f"    {y}: [\n")
        # add imports
        template.pop(0)
        for y in existing_years[::-1]:
            template.insert(0, f"import _{y}\n")
        with fp.open("w") as f:
            f.writelines(template)

        # add to existing solutions file
        fp = Path("data/solution_list.txt")
        with fp.open("r+") as f:
            lines = set(f.readlines())
            lines.add(f"{year}/{day}\n")
            f.seek(0)
            f.truncate(0)
            f.writelines(sorted(list(lines)))


def run_part(year: int, day: int, part: str):
    year = str(year)
    day = day_to_str(day)

    if not check_exists(year, day):
        print("Day does not exist")

    else:
        with open("data/SESSION.txt", "r") as f:
            session = f.read()
        data = get_data(session, int(day), int(year))
        solution = Solution(int(year), int(day))

        if part == "a": print(solution.solvePartA(data))
        elif part == "b": print(solution.solvePartB(data))


def validate(s: Settings):
    if s.validate:
        while True:
            i = input("Are you sure? ('y' or 'n'): ")
            match i:
                case "y":
                    return True
                case "n":
                    return False
                case _:
                    print("invalid answer")
    else:
        return True


class Settings:
    cur = []
    validate = True


def main():
    settings = Settings()

    while True:
        cmd = input("\nAOCshell: ")
        if cmd.lower() != cmd:
            print("Please don't use capital letters")
        else:
            match cmd.split():
                case ["setcur", year, day, part]:
                    settings.cur = [int(year), int(day), part]
                    print(f"set current run file to year {year}, day {day}, part {part}")

                case ["setcur", *_]:
                    print("incorrect use of 'setcur': should be 'setcur <year> <day> <part>'")

                case ["run", year, day, part]:
                    print(f"running year {year}, day {day}, part {part}")
                    run_part(int(year), int(day), part)

                case ["run"]:
                    if settings.cur:
                        print("running year {}, day {}, part {}".format(*settings.cur))
                        run_part(*settings.cur)
                    else:
                        print("No current file selected")

                case ["run", *_]:
                    print("incorrect use of 'run': should be 'run' or 'run <year> <day> <part>'")

                case ["toggleconfirm"]:
                    settings.validate = not settings.validate
                    print(f"toggled confirm to {settings.validate}")

                case ["toggleconfirm", *_]:
                    print("incorrect use of 'confirm': takes no arguments")

                case [c, *_]:
                    print(f"Unknown command: '{c}'")


if __name__ == "__main__":
    main()
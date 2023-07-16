from pathlib import Path


def _get_existing():
    fp = Path("data/solution_list.txt")
    with fp.open("r") as f:
        existing = f.read().split("\n")
    solutions = [d.split("/") for d in sorted(existing)]
    existing_years = set()
    for year, _ in solutions:
        existing_years.add(year)
    return solutions, sorted(list(existing_years))


def create_day(year: int, day: int):
    year = str(year)
    day = "0" if day < 10 else "" + str(day)

    existing_solutions, existing_years = _get_existing()

    if [year, day] in existing_solutions:
        print("Already exists")
        return
    else:
        print("creating...")
        return
        module_path = Path(f"_{year}")
        solution_file_path = module_path / f"Day{day}.py"

        # create file
        fp = Path("data/solution_template.txt")
        with fp.open("r") as f:
            template = f.read()
        with solution_file_path.open("w") as f:
            f.writelines(template)

        # redo __init__ file
        fp = module_path / "__init__.py"
        with fp.open("r+") as f:
            lines = f.readlines()
            lines.append(f"from . import Day{day}\n")
            f.writelines(sorted(lines))

        # redo solutions.py file
        fp = Path("data/solution_list_template.txt")
        with fp.open("r") as f:
            template = f.readlines()
        fp = Path("solutions.py")
        with fp.open("w") as f:
            # add to _solutions dict
            template.pop(3)
            for y in existing_years[::-1]:
                days = [day for year, day in existing_years if year == y]
                template.insert(3, "\t],\n")
                for d in days[::-1]:
                    template.insert(f"\t\t(_{y}.Day{d}.solvePartA, _{y}.Day{d}.solvePartB),\n")
                template.insert(3, f"\t{y}: [\n")
            # add imports
            template.pop(0)
            for y in existing_years[::-1]:
                template.insert(0, f"import _{y}\n")


create_day(2021, 10)

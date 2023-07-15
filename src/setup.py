from pathlib import Path

DAY = "08"
YEAR = "2021"


MODULE_PATH = Path(f"_{YEAR}")
SOLUTION_FILE_PATH = MODULE_PATH / f"Day{DAY}.py"

if not SOLUTION_FILE_PATH.is_file():

    # create file
    with open("template.py", "r") as f:
        TEMPLATE = f.read()
    with SOLUTION_FILE_PATH.open("w") as f:
        f.writelines(TEMPLATE)

    # append file to __init__ of module
    fp = MODULE_PATH / "__init__.py"
    with fp.open("a") as f:
        f.write(f"from . import Day{DAY}\n")

    # # insert into solution.py
    # p = Path(f"solution.py")
    # with p.open("r") as f:
    #     print(f.readlines()[:-11])

    print(f"Added {YEAR}, Day {DAY}")

else: print("Day already exists")

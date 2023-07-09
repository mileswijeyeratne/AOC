from aocd import get_data

with open("SESSION.txt", "r") as f:
    SESSION = f.read()

YEAR = "2021"
DAY = "04"

PART = input("Part 'a' or 'b'?\n\t>>> ").upper().strip(" ")


class Solution:
    """Scuffed class to stop syntax error for non existant instance of solution"""
    def solvePartA(self, _): return "solution does not exist"

    solvePartB = solvePartA


exec(f"from _{YEAR} import Day{DAY} as Solution")

data = get_data(session=SESSION, day=int(DAY), year=int(YEAR))

if PART == "A":
    print(Solution.solvePartA(data))
elif PART == "B":
    print(Solution.solvePartB(data))
else:
    print("Invalid part")

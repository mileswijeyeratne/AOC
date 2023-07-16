from aocd import get_data
from solutions import Solution

try:
    with open("SESSION.txt", "r") as f:
        SESSION = f.read()
except FileNotFoundError:
    raise Exception("session file does not exist")

YEAR = "2021"
DAY = "09"

data = get_data(SESSION, int(DAY), int(YEAR))
solution = Solution(int(YEAR), int(DAY))

print(f"{YEAR}: Day {DAY}")

PART = input("Part 'a' or 'b'?\n\t>>> ").upper().strip(" ")

if PART == "A":
    print(solution.solvePartA(data))
elif PART == "B":
    print(solution.solvePartB(data))
else:
    print("Invalid part")
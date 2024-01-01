def _parse_data(data):
    return [int(d) for d in data.strip("\n").split(",")]


def _solve(data, days):
    data = _parse_data(data)

    fish = {i: 0 for i in range(9)}
    for f in data: fish[f] += 1

    for day in range(days):
        new = {i: 0 for i in range(9)}

        for age, amount in fish.items():
            if age == 0:
                new[8] += amount
                new[6] += amount
            else:
                new[age-1] += amount

        fish = new.copy()

    return sum([amount for _, amount in fish.items()])

def solvePartA(data):
    return _solve(data, 80)

def solvePartB(data):
    return _solve(data, 256)


if __name__ == "__main__":
    test = """3,4,3,1,2"""

    print(solvePartB(test))
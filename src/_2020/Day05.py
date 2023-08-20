def _parse_data(data):
    return data.split("\n")


def _to_id(seat):
    return int(seat.replace("B", "1").replace("F", "0").replace("R", "1").replace("L", "0"), 2)


def solvePartA(data):
    data = _parse_data(data)

    return max([_to_id(s) for s in data])


def solvePartB(data):
    data = _parse_data(data)

    ids = sorted([_to_id(s) for s in data])

    for a, b in zip(ids, ids[1:]):
        if b - a == 2:
            return a + 1

    return "No Seat"


if __name__ == "__main__":
    test = """BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
BFFFBBFRLR"""

    print(solvePartB(test))

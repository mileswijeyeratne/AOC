from statistics import median

def _parse_data(data):
    return [int(i) for i in data.strip("\n").split(",")]


def solvePartA(data):
    data = _parse_data(data)
    med = median(data)
    return int(sum([abs(med - i) for i in data]))


def solvePartB(data):
    data = _parse_data(data)

    cur_best = float("inf")

    for c in range(min(data), max(data)+1):
        total = 0
        for i in data:
            steps = abs(c-i)
            total += steps * (steps+1) / 2
        cur_best = min(total, cur_best)

    return cur_best


if __name__ == "__main__":
    test = """16,1,2,0,4,2,7,1,2,14"""

    print(solvePartB(test))
def _parse_data(data):
    res = []
    for line in data.split("\n"):
        policy, pswd = line.split(":")
        policy = policy.replace(" ", "-").split("-")
        policy[:2] = [int(c) for c in policy[:2]]
        res.append((policy, pswd[1:]))
    return res


def solvePartA(data):
    data = _parse_data(data)

    res = 0

    for policy, pswd in data:
        l, u, c = policy
        if l <= pswd.count(c) <= u:
            res += 1

    return res


def solvePartB(data):
    data = _parse_data(data)

    res = 0

    for policy, pswd in data:
        l, u, c = policy
        if (pswd[l-1] == c) ^ (pswd[u-1] == c):
            res += 1

    return res


if __name__ == "__main__":
    test = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""

    print(solvePartB(test))

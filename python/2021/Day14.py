from collections import Counter


def _parse_data_naive(data):
    start, pairs = data.split("\n\n")
    pairs = [p.split(" -> ") for p in pairs.split("\n")]
    pairs = {tuple(k): v for k, v in pairs}
    return start, pairs


def _step_naive(string, pairs: dict):
    res = string[0]
    for a, b in zip(string, string[1:]):
        res += pairs.get((a, b), "")
        res += b
    return res


def _solve_naive(data, steps):
    polymer, pairs = _parse_data_naive(data)

    for _ in range(steps):
        polymer = _step_naive(polymer, pairs)

    c = Counter(polymer)
    min_c = float("inf")
    max_c = 0
    for _, v in c.items():
        min_c = min(min_c, v)
        max_c = max(max_c, v)

    return max_c - min_c


def solvePartA(data):
    return _solve_naive(data, 10)


def _parse_data(data):
    start, pairs = data.split("\n\n")
    first_and_last = start[0], start[-1]
    start = Counter(zip(start, start[1:]))
    pairs = [p.split(" -> ") for p in pairs.split("\n")]
    pairs = {tuple(k): [(k[0], v), (v, k[1])] for k, v in pairs}
    return start, pairs, first_and_last


def _step(poly, pairs):
    new_poly = {}
    for k, v in poly.items():
        for nk in pairs[k]:
            new_poly[nk] = v + new_poly.get(nk, 0)
    return new_poly


def _count(poly, f, l):
    res = {}
    for pair, count in poly.items():
        for char in pair:
            res[char] = count + res.get(char, 0)
    res[f] += 1
    res[l] += 1
    return (max(res.values()) - min(res.values())) // 2


def solvePartB(data):
    poly, pairs, first_and_last = _parse_data(data)

    for _ in range(40):
        poly = _step(poly, pairs)

    return _count(poly, *first_and_last)


if __name__ == "__main__":
    test = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

    print(solvePartB(test))

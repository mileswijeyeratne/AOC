"""
https://adventofcode.com/2022/day/13
"""

TESTDATA = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""


def _group(iterable, n):
    return [iterable[i: i+n] for i in range(0, len(iterable), n)]


def _parse_data(data):
    data = [eval(line) for line in data.split("\n") if line != ""]
    pairs = _group(data, 2)
    return pairs

def _compare(l_in, r_in):
    if isinstance(l_in, list): l = l_in[::]
    else: l = l_in
    if isinstance(r_in, list): r = r_in[::]
    else: r = r_in
    if isinstance(l, int) and isinstance(r, int):
        if l == r:
            return None
        else:
            return l < r
    if isinstance(l, list) and isinstance(r, list):
        while True:
            if len(l) == 0 and len(r) == 0: return None
            if len(l) == 0: return True
            if len(r) == 0: return False
            nl = l.pop(0)
            nr = r.pop(0)
            res = _compare(nl, nr)
            if res is not None: return res
    else:
        return _compare(l if isinstance(l, list) else [l], r if isinstance(r, list) else [r])

def A(data):
    data = _parse_data(data)
    res = 0
    for i, pair in enumerate(data):
        # print(i+1, end="\n\t")
        # print(pair, end="\n\t")
        a = _compare(*pair)
        # print(a, end="\n\n")
        if a: res += i+1

    return res

def _bubble_sort(array):
    # credit https://realpython.com/sorting-algorithms-python/
    n = len(array)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if not _compare(array[j], array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted:
            break

    return array

def B(data):
    pairs = _parse_data(data)
    items = []
    for pair in pairs:
        items.extend(pair)
    items.extend([[[2]], [[6]]])

    ordered = _bubble_sort(items)

    return (ordered.index([[2]])+1) * (ordered.index([[6]])+1)


if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run AOC day 13")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    input_data = TESTDATA if args.t else aocd.get_data(
        session="53616c7465645f5f6a8cadc93b9182aac8706b0eaa2c354155a2097c65ae98ce052bb1a6d2f55bc96f4b164422ad0e9fdd7b28dadeb8e47a29204fa7d603cbaf",
        day=13,
        year=2022)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print("Program finished in", time_taken, "seconds")
    print(res)
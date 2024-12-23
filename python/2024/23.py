"""
https://adventofcode.com/2024/day/23

      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 23   00:08:00    810      0   00:39:49   1795      0

decent p1
part 2 my naive way just didn't finish
worked out it was a find maximal fully connected subgraph pretty quick
took me a bit of research to find the right algorithm and had an implementation
bug that slowed me down
"""

from collections import defaultdict

TESTDATA = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""


def _parse_data(data):
    conns = defaultdict(set)
    for line in data.split("\n"):
        a, b = line.split("-")
        conns[a].add(b)
        conns[b].add(a)
    return conns


def A(data):
    conns = _parse_data(data)

    res = set()

    for a in conns:
        for b in conns[a]:
            for c in conns[a]:
                if b == c:
                    continue
                if b not in conns[c]:
                    continue
                if not (a[0] == "t" or b[0] == "t" or c[0] == "t"):
                    continue
                res.add(tuple(sorted((a, b, c))))

    return len(res)


def B(data):
    conns = _parse_data(data)

    def bron_kerbosch(R, P, X):
        # https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
        res = set()
        if not P | X:
            res = R
        PC = P.copy()
        for v in P:
            if (found := bron_kerbosch(R | {v}, PC & conns[v], X & conns[v])) is not None:
                if len(found) > len(res):
                    res = found
            PC.remove(v)
            X.add(v)
        return res

    return ",".join(sorted(bron_kerbosch(set(), set(conns.keys()), set())))


if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    import os
    parser = ArgumentParser(description="Run AOC day 1")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    session = os.environ.get("aoc-session")
    assert session is not None, "Please set 'aoc-session' environment variable"

    input_data = TESTDATA if args.t else aocd.get_data(
        session=session,
        day=23,
        year=2024)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)

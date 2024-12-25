"""
https://adventofcode.com/2024/day/24

      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 24   00:12:54    630      0   23:31:52   9606      0

HOLY THAT WAS A DAY
lowkey fun ibr
little scripting to parse the tree into a format graphviz can run on
then just manually looked through the full adder circuits until i found errors
"""

TESTDATA = """x00: 0
x01: 1
x02: 0
x03: 1
x04: 0
x05: 1
y00: 0
y01: 0
y02: 1
y03: 1
y04: 0
y05: 1

x00 AND y00 -> z05
x01 AND y01 -> z02
x02 AND y02 -> z01
x03 AND y03 -> z03
x04 AND y04 -> z04
x05 AND y05 -> z00"""


def _parse_data(data):
    _start, _wires = data.split("\n\n")
    start = {}
    for line in _start.split("\n"):
        k, v = line.split(": ")
        start[k] = int(v)
    wires = {}
    for line in _wires.split("\n"):
        v, k = line.split(" -> ")
        wires[k] = v.split()
    return start, wires


def num(s, states):
    return int("".join(str(states[w]) for w in sorted(
        (w for w in states if w.startswith(s)), reverse=True)), 2)


def dfs(wire, states, wires):
    if wire in states:
        return states[wire]
    lhs, _op, rhs = wires[wire]
    lhs, rhs, = dfs(lhs, states, wires), dfs(rhs, states, wires)
    if _op == "AND":
        def op(x, y): return x & y
    if _op == "OR":
        def op(x, y): return x | y
    if _op == "XOR":
        def op(x, y): return x ^ y
    res = op(lhs, rhs)
    states[wire] = res
    return res


def A(data):
    states, wires = _parse_data(data)

    for wire in wires:
        if wire.startswith("z"):
            dfs(wire, states, wires)

    return num("z", states)


def B(data):
    states, wires = _parse_data(data)

    incorrect_pairs = [("z07", "vmv"), ("z20", "kfm"),
                       ("z28", "hnv"), ("hth", "tqr")]

    for a, b in incorrect_pairs:
        wires[a], wires[b] = wires[b], wires[a]

    res = open("out.txt", "w")
    res.write("digraph C {\n")

    x = [w for w in states if w.startswith("x")]
    y = [w for w in states if w.startswith("y")]
    z = [w for w in wires if w.startswith("z")]

    res.write("\n")
    for a, b in zip(sorted(x), sorted(y)):
        res.write(f"subgraph {{ rank = same; {a}; {b} }}\n")
    res.write(f"subgraph {{ rank = same; {'; '.join(sorted(z))} }}\n")

    for w in sorted(wires.keys()):
        a, op, b = wires[w]
        res.write(f'{a} -> {w} [ label="{op}" ];\n')
        res.write(f'{b} -> {w} [ label="{op}" ];\n')

    res.write("}\n")

    res.close()

    a = num("x", states)
    b = num("y", states)
    for wire in wires:
        if wire.startswith("z"):
            dfs(wire, states, wires)
    r = num("z", states)

    return a + b == r


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
        day=24,
        year=2024)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)

"""
https://adventofcode.com/2023/day/25
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 25   01:13:19   1704      0   01:13:28   1461      0

(took alot of graph theory research and alot of searching the networkx docs)
"""

from collections import defaultdict
import networkx as nw 

TESTDATA = """jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr"""

def _parse_data(data):
    res = defaultdict(set)
    for line in data.split("\n"):
        start, targets = line.split(": ")
        targets = targets.split()
        for t in targets:
            res[t].add(start)
            res[start].add(t)
    return res


def A(data):
    data = _parse_data(data)
    
    graph = nw.Graph()

    for node1 in data:
        for node2 in data[node1]:
            graph.add_edge(node1, node2)

    cuts = nw.minimum_edge_cut(graph)

    assert len(cuts) == 3

    for cut in cuts:
        graph.remove_edge(*cut)

    prod = 1
    for subgraph in nw.connected_components(graph):
        prod *= len(subgraph)

    return prod


def B(_):
    return "No part B!"


if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run AOC day 25")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    try:
        with open("../session.txt") as f:
            session = f.read().strip()
    except:
        with open("session.txt") as f:
            session = f.read().strip()
    input_data = TESTDATA if args.t else aocd.get_data(
        session=session,
        day=25,
        year=2023)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)
"""
https://adventofcode.com/2023/day/8
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
  8   02:38:47  18273      0   03:17:54  12366      0

(I didn't intend to do the problem until the evening but I looked at it over breakfast and then wanted to do it.
 I also had a break between part a and b)
  8   00:08:00                 00:20:00    <- Approximate times actually spent coding
"""

from math import lcm

TESTDATA = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


def _parse_data(data):
    instructions, nodes = data.replace("(", "").replace(")", "").split("\n\n")
    nodes = [line.split(" = ") for line in nodes.split("\n")]
    nodes = {node[0]: node[1].split(", ") for node in nodes}
    return instructions, nodes


def A(data):
    instructions, nodes = _parse_data(data)

    cur_node = "AAA"
    count =0 

    while True:
        c = instructions[count % len(instructions)]
        count += 1
        if c == "L":
            cur_node = nodes[cur_node][0]
        else:
            cur_node = nodes[cur_node][1]

        if cur_node == "ZZZ":
            return count


# finds cycles and takes the lcm (question was unclear that this would even work, i just assumed it would work on the full data aswell as the test)
def B(data):
    instructions, nodes = _parse_data(data)

    cur_nodes = [k for k in nodes.keys() if k[-1] == "A"]
    periods = [0 for _ in cur_nodes]
    count = 0 

    while not all([p!=0 for p in periods]):
        c = instructions[count % len(instructions)]
        count += 1
        if c == "L":
            cur_nodes = [nodes[n][0] for n in cur_nodes]
        else:
            cur_nodes = [nodes[n][1] for n in cur_nodes]

        for i, node in enumerate(cur_nodes):
            if node[-1] == "Z" and periods[i] == 0:
                periods[i] = count

    return lcm(*periods)
    



if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run AOC day 8")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    with open("../session.txt") as f:
        session = f.read().strip()
    input_data = TESTDATA if args.t else aocd.get_data(
        session=session,
        day=8,
        year=2023)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)
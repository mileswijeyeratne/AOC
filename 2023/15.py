"""
https://adventofcode.com/2023/day/15
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 15   00:04:58   1222      0   00:23:35   1355      0

Could've done part a faster if I hadn't misread 17 as 7 lmao
"""

TESTDATA = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""


def _parse_data(data):
    return data.strip("\n").split(",")


def _hash(word):
    res = 0
    for c in word:
        res += ord(c)
        res *= 17
        res %= 256
    return res


def A(data):
    data = _parse_data(data)

    res = 0

    for word in data:
        print(word, _hash(word))
        res += _hash(word)

    return res


def B(data):
    data = _parse_data(data)

    boxes = {}

    for word in data:
        splitchar = "=" if "=" in word else "-"
        label, number = word.split(splitchar)
        box = _hash(label)
        
        if splitchar == "=":
            items = boxes.get(box, [])
            replaced = False
            for i, item in enumerate(items):
                if item[0] == label:
                    items[i] = label, int(number)
                    replaced = True
            
            if not replaced:
                items += [(label, int(number))]

            boxes[box] = items

        elif splitchar == "-":
            boxes[box] = [item for item in boxes.get(box, []) if item[0] != label]

    res = 0

    for box_num, contents in boxes.items():
        res += (box_num + 1) * sum((i+1)*v[1] for i, v in enumerate(contents))

    return res


if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run AOC day 15")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    with open("../session.txt") as f:
        session = f.read().strip()
    input_data = TESTDATA if args.t else aocd.get_data(
        session=session,
        day=15,
        year=2023)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)
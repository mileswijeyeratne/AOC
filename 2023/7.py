"""
https://adventofcode.com/2023/day/7
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
  7   00:30:56   2661      0   00:49:21   2669      0

Lots of problems today:
    - No internet
    - aocd din't work with hotspot
    - I used match without realising my python version when running in cmd is 3.8
"""

from collections import Counter

TESTDATA = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

card_values = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

hand_types = {
    "5": 5,
    "4": 4,
    "f": 3,
    "3": 2,
    "2": 1,
    "1": 0,
    "h": -1,
}

def _compare_value(l_value, r_value):
    if card_values[l_value] == card_values[r_value]: return None
    return card_values[l_value] > card_values[r_value]

def _hand_type(hand, part_b=False):
    c = Counter(hand)
    v = sorted(c.values(), reverse=True)
    if part_b:
        jacks = c.get("J", 0)
        if jacks == 5: return "5"
        if jacks > 0:
            v.remove(jacks)
            v[0] += jacks
    match v:
        case [5]: 
            return "5"
        case [4, _]: 
            return "4"
        case [3, 2]: 
            return "f"
        case [3, 1, 1]: 
            return "3"
        case [2, 2, 1]: 
            return "2"
        case [2, 1, 1, 1]:
            return "1"
        case [1, 1, 1, 1, 1]: 
            return "h"
        case _: 
            raise ValueError(f"Bad case: {c}, {c.values()}")

def _compare_hand(l_hand_in, r_hand_in, part_b=False):
    l_hand, r_hand = l_hand_in[0], r_hand_in[0]
    l_val, r_val = hand_types[_hand_type(l_hand, part_b)], hand_types[_hand_type(r_hand, part_b)]
    if l_val < r_val: return False
    if l_val > r_val: return True
    else:
        for i in range(len(l_hand)):
            l_c, r_c = l_hand[i], r_hand[i]
            res = _compare_value(l_c, r_c)
            if res is not None:
                return res
        print(f"Hand {l_hand} and {r_hand} are equal")
    
def _bubble_sort(array, part_b=False):
    # credit https://realpython.com/sorting-algorithms-python/
    n = len(array)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if not _compare_hand(array[j], array[j + 1], part_b):
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted:
            break

    return array

def _parse_data(data):
    return [line.split(" ") for line in data.split("\n")]

def _solve(data, part_b=False):
    data = _parse_data(data)
    data = _bubble_sort(data, part_b)
    res = 0
    for i, (_, v) in enumerate(data[::-1]):
        res += (i+1) * int(v)
    return res

def A(data):
    return _solve(data, False)

def B(data):
    return _solve(data, True)

if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run AOC day 7")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()
    
    with open("../session.txt") as f:
        session = f.read().strip()
    input_data = TESTDATA if args.t else aocd.get_data(
        session=session,
        day=7,
        year=2023)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)
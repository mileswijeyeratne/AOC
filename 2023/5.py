"""
https://adventofcode.com/2023/day/5
      -------Part 1--------   -------Part 2--------
Day       Time  Rank  Score       Time  Rank  Score
  5   00:26:42  2421      0   01:59:02  4312      0
"""

TESTDATA = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

def _parse_data(data):
    seeds = []
    rules = []

    data = data.split("\n")
    for num in data.pop(0)[7:].split():
        seeds.append(int(num))
    data.pop(0)

    cur_rule = {}
    while data:
        row = data.pop(0)
        if row == "":
            rules.append(cur_rule)
        elif row[-5:] == " map:":
            cur_rule = {}
        else:
            row = list(map(int, row.split()))
            cur_rule[(row[1], row[1] + row[-1])] = row[0] - row[1]
    
    if cur_rule: rules.append(cur_rule)

    return seeds, rules

def _apply_rule(num, rule):
    for (start_range, mapped_range), inc in rule.items():
        if start_range <= num < mapped_range:
            return num + inc
    return num

def A(data):
    nums, rules = _parse_data(data)
    res = []
    print(nums)

    for num in nums:
        for rule in rules:
            num = _apply_rule(num, rule)
        res.append(num)    
    return min(res)


# PART B ATTEMPT 1: ranges
def _apply_rule_fast(num_range, rule_range, inc):
    (a, b), (c, d) = num_range, rule_range
    if a == b: 
        print(f"Empty range {a, b}")
        return None
    if b == c or a == d: return (a, b)
    else: return (a + inc, b + inc)

def _apply_rule_fast_all(num, rule):
    res = []
    for a, b in num:
        for (c, d), inc in rule.items():
            if b <= c < d or c < d <= a:
                # print(f"Ranges {(a, b)} and {(c, d)} didn't overlap: skipping")
                continue
            elif c <= a < b <= d:
                # print("Mapping case 5")
                res.extend(list(filter(lambda x: x is not None, [_apply_rule_fast(pair, (c,d), inc) for pair in [(a, b)]])))
            elif c <= a < d <= b:
                # print(f"Mapping case 2")
                res.extend(list(filter(lambda x: x is not None, [_apply_rule_fast(pair, (c,d), inc) for pair in [(a,d), (d, b)]])))
            elif a < c < b <= d:
                # print("Mapping case 3")
                res.extend(list(filter(lambda x: x is not None, [_apply_rule_fast(pair, (c,d), inc) for pair in [(a,c), (c, b)]])))
            elif a < c < d < b:
                # print("Mapping case 1")
                res.extend(list(filter(lambda x: x is not None, [_apply_rule_fast(pair, (c,d), inc) for pair in [(a,c), (c, d), (d, b)]])))
            else:
                print(f"Unknown case: {(a, b), (c, d)}")
            # print(f"{res=}")
    return res if res else num

def B_with_ranges(data):
    nums, rules = _parse_data(data)
    nums = [tuple(nums[i: i+2]) for i in range(0, len(nums), 2)]
    nums = [[(n[0], n[0] + n[1])] for n in nums]
    res = []
    # print(nums)

    for num in nums:
        # print(f"\nNum: {num}")
        for rule in rules:
            # print(f"\tapplying rule {rule} to {num}")
            num = _apply_rule_fast_all(num, rule)
            # print(f"\tmapped num to {num}\n")
        res.append(num)
    
    m = float("inf")
    for num in res:
        for a, b in num:
            m = min(a, m)

    return m
# END PART B ATTEMPT 1

# PART B ATTEMPT 2: reverse mapping
def B(data):
    nums, rules_normal = _parse_data(data)
    nums = [tuple(nums[i: i+2]) for i in range(0, len(nums), 2)]
    nums = [(n[0], n[0] + n[1]) for n in nums]
    rules = []
    for rule in rules_normal[::-1]:
        new_rule = {}
        for (lb, ub), change in rule.items():
            new_rule[(lb + change, ub + change)] = -change
        rules.append(new_rule)

    for i in range(100_000_000):
        orig = i
        for rule in rules:
            i = _apply_rule(i, rule) # same fn used in part a
        
        for a, b in nums:
            if a <= i < b:
                return orig
    
    return "Something went wrong" # i know upper bound is less than 100_000_000 because of guessing hints given after wrong solutions

if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run AOC day 5")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    with open("../session.txt") as f:
        session = f.read().strip()
    input_data = TESTDATA if args.t else aocd.get_data(session=session, day=5, year=2023)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)
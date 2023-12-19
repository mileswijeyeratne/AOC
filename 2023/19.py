"""
https://adventofcode.com/2023/day/19
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 19   00:25:21   1197      0   01:09:50   1216      0
"""

from dataclasses import dataclass, replace
from typing import List

TESTDATA = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""

@dataclass
class Part:
    x: int
    m: int
    a: int
    s: int


@dataclass
class Rule:
    attr: str
    op: str
    val: int
    send_to: str


def _parse_data(data):
    workflows_, parts = data.split("\n\n")

    workflows = {}

    for w in workflows_.split("\n"):
        w_name, rules_ = w[:-1].split("{")
        rules = []
        for rule in rules_.split(","):
            if ":" not in rule:
                rules.append(Rule("x", ">", -1, rule))
                continue

            op = "<" if "<" in rule else ">"
            name, other = rule.split(op)
            val, send_to = other.split(":")
            rules.append(Rule(name, op, int(val), send_to))
        workflows[w_name] = rules

    parts = [eval(f"Part({part[1:-1]})") for part in parts.split("\n")]  # lovely safe code with eval() - I'm sure Eric won't give dangerous data right..

    return workflows, parts


def A(data):
    workflows, parts = _parse_data(data)

    accepted_parts = []
    rejected_parts = []

    for part in parts:
        workflow_name = "in"
        while workflow_name not in "AR":
            workflow: List[Rule] = workflows[workflow_name]
            for rule in workflow:
                comp_attr = None
                if rule.attr == "x": comp_attr = part.x
                elif rule.attr == "m": comp_attr = part.m
                elif rule.attr == "a": comp_attr = part.a
                elif rule.attr == "s": comp_attr = part.s

                if rule.op == ">":
                    if comp_attr > rule.val:
                        workflow_name = rule.send_to
                        break
                
                if rule.op == "<":
                    if comp_attr < rule.val:
                        workflow_name = rule.send_to
                        break

        if workflow_name == "A":
            accepted_parts.append(part)
            print("A")
        elif workflow_name == "R":
            rejected_parts.append(part)
            print("R")

    return sum([p.x+p.m+p.a+p.s for p in accepted_parts])

@dataclass
class RangePart:
    x: (int, int)
    m: (int, int)
    a: (int, int)
    s: (int, int)


def split_range(lb, ub, n, op):
    if n < lb:
        res = [((lb, ub), ">" == op)]
    elif n > ub:
        res = [((lb, ub), "<" == op)]
    else:
        ls = n-1 if op == "<" else n
        us = n+1 if op == ">" else n
        res = [
            ((lb, ls), op == "<"),
            ((us, ub), op == ">")
        ]
    return [r for r in res if r[0][0] <= r[0][1]]


def B(data):
    workflows, _ = _parse_data(data)
    
    checking_parts = [(RangePart(*([(1, 4000)]*4)), "in")]
    accepted_parts = []
    
    while checking_parts:
        part, workflow_name = checking_parts.pop()

        if workflow_name == "A":
            accepted_parts.append(part)
            continue

        if workflow_name == "R":
            continue

        workflow: List[Rule] = workflows[workflow_name]

        def apply_rules(workflow: List[Rule], part):
            rule = workflow[0]
            comp_attr = None
            if rule.attr == "x": comp_attr = part.x
            elif rule.attr == "m": comp_attr = part.m
            elif rule.attr == "a": comp_attr = part.a
            elif rule.attr == "s": comp_attr = part.s            

            for new_range, passes in split_range(*comp_attr, rule.val, rule.op):
                if rule.attr == "x": new_part = replace(part, x=new_range)
                elif rule.attr == "m": new_part = replace(part, m=new_range)
                elif rule.attr == "a": new_part = replace(part, a=new_range)
                elif rule.attr == "s": new_part = replace(part, s=new_range)
            
                if passes:
                    checking_parts.append((new_part, rule.send_to))
                else:
                    apply_rules(workflow[1:], new_part)
            
        apply_rules(workflow, part)

    res = 0
    for p in accepted_parts:
        prod = 1
        for lb, ub in [p.a, p.x, p.m, p.s]:
            prod *= ub - lb + 1
        res += prod

    return res


if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run AOC day 19")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    with open("../session.txt") as f:
        session = f.read().strip()
    input_data = TESTDATA if args.t else aocd.get_data(
        session=session,
        day=19,
        year=2023)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)
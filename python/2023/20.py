"""
https://adventofcode.com/2023/day/20
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 20   01:32:32   2786      0   03:13:35   2549      0

(I started at around 0:30:00 and then spent 45 mins letting my brute force solution run before coming back and doing it well)
 20   01:02:32                 02:43:35    <- Approximate actual times
"""

# Note: - This solution is hardcoded to work on my data
#       - Lines 173 and 183 will need changing to work on any other data

from dataclasses import dataclass
from typing import List, Dict

# TESTDATA = r"""broadcaster -> a, b, c
# %a -> b
# %b -> c
# %c -> inv
# &inv -> a"""

TESTDATA = r"""broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""

@dataclass
class Pulse:
    type: bool
    came_from: str
    target: str

class Module:
    def __init__(self, name: str, next: List[str]):
        self.name = name
        self.next = next
    
    # I want to learn how the ABC module works because this method seems a bit out of place
    def pulse(self, pulse: Pulse) -> List[Pulse]:
        raise NotImplemented

    @staticmethod
    def create(type: str, name: str, next: List[str]):
        if type == "b":
            return BroadCaster("broadcaster", next)
        elif type == "%":
            return FlipFlop(name, next)
        elif type == "&":
            return Conjunction(name, next)
        else:
            raise ValueError(f"[Modude.create()] Unexpected type: {type}")
    
class FlipFlop(Module):
    def __init__(self, name, next):
        super().__init__(name, next)
        self.state = {}
    
    def pulse(self, pulse: Pulse):
        res = []
        if pulse.type == False:
            self.state = not self.state
            res.extend([Pulse(self.state, self.name, t) for t in self.next])
        return res

class Conjunction(Module):
    def __init__(self, name, next):
        super().__init__(name, next)
        self.state = {}
    
    def pulse(self, pulse: Pulse):
        self.state[pulse.came_from] = pulse.type

        if all(v for v in self.state.values()):
            state = False
        else:
            state = True

        return [Pulse(state, self.name, t) for t in self.next]

class BroadCaster(Module):
    def __init__(self, name: str, next: List[str]):
        super().__init__(name, next)

    def pulse(self, pulse: Pulse):
        return [Pulse(pulse.type, self.name, t) for t in self.next]

def _parse_data(data):
    res = {}

    for row in data.split("\n"):
        module, targets = row.split(" -> ")
        module_type, name = module[0], module[1:]
        targets = targets.split(", ")
        if name == "roadcaster": name = "broadcaster"
        
        res[name] = Module.create(module_type, name, targets)
    
    # which modules lead to a conjunction
    for n, m in res.items():
        if isinstance(m, Conjunction):
            m.state = {name: False for (name, mod) in res.items() if n in mod.next}

    return res


def A(data):
    modules: Dict[str, Module] = _parse_data(data)

    num_low = 0
    num_high = 0

    for _ in range(1000):

        pulse_q = [Pulse(False, "", "broadcaster")]

        while pulse_q:
            p = pulse_q.pop(0)
            if p.type == False:
                num_low += 1
            else: num_high += 1

            if p.target in modules:
                pulse_q.extend(modules[p.target].pulse(p))

    return num_high * num_low


def B_brute_foce(data):
    # my back-of-the-envelope maths says this will take 28.5 millenia to complete lmao
    # runs about 100,000 steps in 6 secs, answer was arohnd 2.5x10^14 so take 1.5x10^10 secs to complete
    modules: Dict[str, Module] = _parse_data(data)

    res = 0

    while True:
        res += 1

        if res % 100000 == 0: print(res)

        pulse_q = [Pulse(False, "", "broadcaster")]

        while pulse_q:
            p = pulse_q.pop(0)

            if p.target == "rx" and p.type == False:
                return res

            if p.target in modules:
                pulse_q.extend(modules[p.target].pulse(p))

def B(data):
    # uses cycles and a bit of hard coding on my data
    modules: Dict[str, Module] = _parse_data(data)

    res = 0

    cycle_lens = {}

    while True:
        res += 1

        if res % 100000 == 0: print(res)

        pulse_q = [Pulse(False, "", "broadcaster")]

        while pulse_q:
            p = pulse_q.pop(0)

            if p.target == "rx" and p.type == False:
                return res

            if len(cycle_lens.keys()) == 4:  # my input has exactly 4 modules that precede "rx"
                res = 1
                for v in cycle_lens.values(): res *= v
                return res

            if p.target in modules:
                new_pulses = modules[p.target].pulse(p)
                pulse_q.extend(new_pulses)

                # if getting sent from a node that precedes to rx and that node is sending a low signal
                if new_pulses and new_pulses[0].type == True and p.target in ["cl", "rp", "lb", "nj"]:  # found by looking at input
                    if cycle_lens.get(p.target, None) is None:
                        cycle_lens[p.target] = res
                    
if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run AOC day 20")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    with open("../session.txt") as f:
        session = f.read().strip()
    input_data = TESTDATA if args.t else aocd.get_data(
        session=session,
        day=20,
        year=2023)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)
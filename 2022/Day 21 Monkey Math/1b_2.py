
class Solver():
    def __init__(self, monkeys):
        self.monkeys = monkeys
        self.loops = 0
    
    def eval_monkey(self, monkey):
        if not str(self.monkeys[monkey]).strip("-").isnumeric():
            a = self.monkeys[self.monkeys[monkey][:4]]
            b = self.monkeys[self.monkeys[monkey][7:]]
            operator = self.monkeys[monkey][5]
            if monkey == "root": operator = "=="

            if (str(a).isnumeric() or type(a) is int) and (str(b).isnumeric() or type(b) is int):
                value = int(eval(str(a) + operator + str(b)))
                self.monkeys[monkey] = value
    
    def solve(self):
        while not type(self.monkeys["root"]) is bool:
            for key in self.monkeys:
                self.eval_monkey(key)
            self.loops += 1

        return self.monkeys["root"]


def test(input):
    data = [(line.strip()[:4], line.strip()[6:]) for line in open("Day 21/rawData.txt")]
    monkeys = {}
    for monkey, command in data:
        monkeys[monkey] = command
        monkeys["humn"] = input
    solve = Solver(monkeys)
    result = solve.solve()
    print(f"{input} gives a result of {result}")
    return result

if __name__ == "__main__":
    for i in range(50, 302):
        if test(i):
            print(f"found solution {i}")

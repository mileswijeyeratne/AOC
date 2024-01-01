data = [(line.strip()[:4], line.strip()[6:]) for line in open("Day 21/rawData.txt")]

monkeys = {}
for monkey, command in data:
    monkeys[monkey] = command


def eval_monkey(monkey):
    if not str(monkeys[monkey]).isnumeric():
        a = str(monkeys[monkeys[monkey][:4]])
        b = str(monkeys[monkeys[monkey][7:]])
        operator = monkeys[monkey][5]

        if a.isnumeric() and b.isnumeric():
            expression = a + operator + b
            monkeys[monkey] = int(eval(expression))

loops = 0

while not str(monkeys["root"]).isnumeric():
    for key in monkeys:
        eval_monkey(key)
    loops += 1

print(loops)
print("done")
print(monkeys["root"])
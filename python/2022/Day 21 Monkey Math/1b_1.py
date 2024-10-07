data = [(line.strip()[:4], line.strip()[6:]) for line in open("Day 21/rawData.txt")]

monkeys = {}

def reset_monkeys(humn):
    monkeys = {}
    for monkey, command in data:
        monkeys[monkey] = command
    monkeys["humn"] = humn
    return monkeys

def eval_monkey(monkey):
    if not str(monkeys[monkey]).isnumeric() and not type(monkeys[monkey]) is int:
        a = str(monkeys[monkeys[monkey][:4]])
        b = str(monkeys[monkeys[monkey][7:]])
        operator = monkeys[monkey][5]
        if monkey == "root": operator = "=="

        if a.isnumeric() and b.isnumeric():
            value = eval(a + operator + b)
            if type(value) is float: value = int(value)
            monkeys[monkey] = value

loops = 0
humn = 0

monkeys = reset_monkeys(humn)


while monkeys["root"] != True:
    if humn >= 1000: break
    humn += 1
    monkeys = reset_monkeys(humn)
    while not type(monkeys["root"]) is bool and loops < 45:  # Part 1 took 40 cycles so if it exceeded 40 then something has gone horribly wrong
        for key in monkeys:
            eval_monkey(key)
        loops += 1
    

print(monkeys["root"])
print(humn)
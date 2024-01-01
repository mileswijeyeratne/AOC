input = [line.strip() for line in open("Day 11/rawData.txt")]
monkey_data = []
cur_monkey = []
for line in input:
    if line == "":
        monkey_data.append(cur_monkey)
        cur_monkey = []
    else: cur_monkey.append(line)
monkey_data.append(cur_monkey)


monkey_rules = [] # List [new worry, divisible by, if False, if True]
monkey_items = [] # List:monkey [ List:item [List:remaindr [remainer for monkey 1, ...], ...], ...]
monkey_inspected = [] # List [int for each monkey]

for monkey in monkey_data:
    monkey_items.append([int(val) for val in monkey[1][15:].strip("").split(",")])
    rules = []
    rules.append(monkey[2][17:].replace("old", "new"))
    rules.append(int(monkey[3][19:]))
    rules.append(int(monkey[5][-1]))
    rules.append(int(monkey[4][-1]))
    monkey_rules.append(rules)
    monkey_inspected.append(0)

monkey_divisivility = [monkey[1] for monkey in monkey_rules]
new_items = []
for monkey in monkey_items:
    temp_monkey = []
    for item in monkey:
        temp_item = []
        for divisiblilty in monkey_divisivility:
            temp_item.append(item%divisiblilty)
        temp_monkey.append(temp_item)
    new_items.append(temp_monkey)
monkey_items = new_items

for i in range(10000):
    for monkey_number, items in enumerate(monkey_items):
        for item_index, _ in enumerate(items):
            # inspect and change worry based on rule increase count of inspected items
            for index, new in enumerate(monkey_items[monkey_number][item_index]): # new is neccesary for the eval to work properly
                monkey_items[monkey_number][item_index][index] = eval(monkey_rules[monkey_number][0])%monkey_divisivility[index]
            monkey_inspected[monkey_number] += 1
            # check if rule holds
            throw_to = int(monkey_items[monkey_number][item_index][monkey_number] == 0) + 2
            monkey_items[monkey_rules[monkey_number][throw_to]].append(monkey_items[monkey_number][item_index])
        monkey_items[monkey_number] = []
    if i % 100 == 0:
        print(f"{i}/10000 processed")

#for index, monkey in enumerate(monkey_items): print(f"{index}: {monkey}")
print(f"monkey_inspected = {monkey_inspected}")

monkey_inspected.sort(reverse=True)
print(monkey_inspected[0]*monkey_inspected[1])
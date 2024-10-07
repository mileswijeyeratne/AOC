input = [line.rstrip("\n") for line in open("Day 3 Rucksack Reorginization/rawData.txt", "r")]


def solve(x):
    split = [[i[:int(len(i)/2)], i[int(len(i)/2):]] for i in input ]
    total = 0
    dupe_item = ""
    for i in split:
        print(i)
        for j in i[0]:
            if j in i[1]:
                dupe_item = j
        if dupe_item.islower():
            total += ord(dupe_item)-96
            print(dupe_item, ord(dupe_item)-96)
        elif dupe_item.isupper():
            total += ord(dupe_item)-38
            print(dupe_item, ord(dupe_item)-38)
    return total


print(solve(input))
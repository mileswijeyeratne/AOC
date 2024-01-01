input = [line.split(" ") for line in open("Day 5 Supply Stacks/rawData.txt", "r")]
start = [
    ["S", "M", "R", "N", "W", "J", "v", "T"],
    ["B", "W", "D", "J", "Q", "P", "C", "V"],
    ["B", "J", "F", "H", "D", "R", "P"],
    ["F", "R", "P", "B", "M", "N", "D"],
    ["H", "V", "R", "P", "T", "B"],
    ["C", "B", "P", "T"],
    ["B", "J", "R", "P", "L"],
    ["N", "C", "S", "L", "T", "Z", "B", "W"],
    ["L", "S", "G"]
]

def solve(x):
    list = start
    for row in x:
        temp = []
        for i in range(int(row[1])):
            temp.append(list[int(row[3])-1].pop())
        while temp:
            list[int(row[5])-1].append(temp.pop())


    arrangement = ""
    for i in list:
        arrangement = arrangement + i[len(i)-1]

    return arrangement


print(solve(input))
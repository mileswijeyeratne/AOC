input = [line.strip().split(" ") for line in open("Day 10/rawData.txt")]

def solve(x):

    cycles = 0
    xvalue = 1
    sum_of_special = 0

    for line in x:
        if line[0] == "noop":
            cycles += 1
        else:
            cycles += 1
            cycles += 1
            xvalue += int(line[1])


print(solve(input))
input = [line.strip("\n").split(" ") for line in open("Day 7 No Space Left On Device/rawData.txt", "r")]

reset = open("Day 7 No Space Left On Device/tempData.txt", "w")
reset.truncate(0)
reset.close()

temp = []
temp.append("/\n")

def solve(x):

    current_dir, depth = "/", 0

    largest_depth = 0

    for line in x:
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "..":
                    if depth != 0 and current_dir != "/":
                        depth -= 1
                        indent_to_check = ""
                        for i in range(depth): indent_to_check = indent_to_check + "\t"
                        for line in temp:
                            if line[:depth+1] == indent_to_check and line[depth+1] != "\t":
                                current_dir = line.split("\t")[-1].split(" ")[0]
                                break
                elif line[2] != "..":
                    depth += 1
                    if depth > largest_depth: largest_depth = depth
                    current_dir = line[2]
        else:
            indent_to_check = ""
            for i in range(depth): indent_to_check = indent_to_check + "\t"
            index = temp.index(indent_to_check + current_dir + "\n")
            indent_to_add = ""
            for i in range(depth+1): indent_to_add = indent_to_add + "\t"
            if line[0] == "dir":
                temp.insert(index+1, indent_to_add + line[1] + "\n")
            elif line[0] != "dir":
                temp.insert(index+1, indent_to_add + line[0] + "\n")
            if depth +1 > largest_depth: largest_depth = depth + 1

    indent_to_check = ""
    for i in range(largest_depth): indent_to_check = indent_to_check + "\t"

    smaller_than_100000_sum = []

    dir_total = 0
    while len(indent_to_check) > 0:
        for line in temp:
            if line[:len(indent_to_check)] == indent_to_check:
                if line.split("\t")[-1].strip("\n").isnumeric():
                    dir_total += int(line.split("\t")[-1].strip("\n"))
            else:
                if dir_total < 100000: smaller_than_100000_sum.append(dir_total)
                dir_total = 0
        indent_to_check = indent_to_check[:-1]
        
    with open("Day 7 No Space Left On Device/tempData.txt", "a") as file:
            for i in temp:
                file.write(i)

    return sum(smaller_than_100000_sum)


print(solve(input))

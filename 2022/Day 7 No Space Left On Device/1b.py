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


    with open("Day 7 No Space Left On Device/tempData.txt", "a") as file:
        for i in temp:
            file.write(i)
    

    indent_to_check = ""
    for i in range(largest_depth): indent_to_check = indent_to_check + "\t"

    dir_sizes = []

    dir_total = 0
    while len(indent_to_check) > 0:
            for line in temp:
                if line[:len(indent_to_check)] == indent_to_check:
                    if line.split("\t")[-1].strip("\n").isnumeric():
                        dir_total += int(line.split("\t")[-1].strip("\n"))
                else:
                    dir_sizes.append(dir_total)
                    dir_total = 0
            indent_to_check = indent_to_check[:-1]

    total = 0
    for line in temp:
        if line.split("\t")[-1].strip("\n").isnumeric():
            total += int(line.split("\t")[-1].strip("\n"))
    dir_sizes.append(total)
    print(f"total is {total}")


    dir_sizes.sort()
    while 0 in dir_sizes: dir_sizes.remove(0)

    size_needed = 30000000 - (70000000 - dir_sizes[-1])

    print(f"size needed is {size_needed}")
    print(f"the directories have sizes: {dir_sizes}")

    for i in dir_sizes:
        if i > size_needed:
            return i

print(solve(input))

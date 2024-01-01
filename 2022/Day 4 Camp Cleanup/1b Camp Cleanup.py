input = [line.split(",") for line in open("Day 4 Camp Cleanup/rawData.txt", "r")]


def solve(x):
    split_list = []
    pairs = 0
    for row in input:
        split_list.append([row[0].split("-"), row[1].rstrip("\n").split("-")])
    for pair in split_list:
        person_1 = [i for i in range(int(pair[0][0]), int(pair[0][1])+1)]
        person_2 = [i for i in range(int(pair[1][0]), int(pair[1][1])+1)]
        print(person_1, person_2)
        overlap = False
        for i in person_1:
            if i in person_2:
                overlap = True
        if overlap:
            pairs += 1
            print(person_1, person_2)
    return pairs


print(solve(input))
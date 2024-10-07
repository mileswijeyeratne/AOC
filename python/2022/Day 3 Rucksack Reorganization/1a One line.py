input = ["vJrwpWtwJgWrhcsFMMfFFhFp",
"jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
"PmmdzqPrVvPwwTWBwg",
"wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
"ttgJtRGJQctTZtZT",
"CrZsJsPPZsGzwwsLwLmpwMDw"]

input = [line.rstrip("\n") for line in open("Day 3 Rucksack Reorganization/rawData.txt", "r")]

# 0 Original
total = 0
chars = []
for line in input:
    halfOne = line[:int(len(line)/2)]
    halfTwo = line[int(len(line)/2):]
    for char in halfOne:
        if char in halfTwo:
            chars.append(char)
            break
for char in chars:
    if char.islower(): total += ord(char) - 96
    else: total += ord(char) - 38
print(total)

# 1 using list comprehension on for loop
total = 0
chars = []
for line in input:
    chars.extend([char for char in line[:int(len(line)/2)] if char in line[int(len(line)/2):]])
for char in chars:
    if char.islower(): total += ord(char) - 96
    else: total += ord(char) - 38
print(total)

# 2 fixing for duplicates
total = 0
chars = []
for line in input:
    chars.extend(list(set([char for char in line[:int(len(line)/2)] if char in line[int(len(line)/2):]])))
for char in chars:
    if char.islower(): total += ord(char) - 96
    else: total += ord(char) - 38
print(total)

# 2.5 removing for loop with list comprehension
                    ### !!! WILL THROW AN ERROR !!! ###
#total = 0
#chars = [list(set([char for char in line[:int(len(line)/2)] if char in line[int(len(line)/2):]])) for line in input]
#for char in chars:
#    if char.islower(): total += ord(char) - 96
#    else: total += ord(char) - 38
#print(total)


# 3 change lists into singe values
total = 0
chars = [list(set([char for char in line[:int(len(line)/2)] if char in line[int(len(line)/2):]]))[0] for line in input]
for char in chars:
    if char.islower(): total += ord(char) - 96
    else: total += ord(char) - 38
print(total)

# 3.5
#total = 0
#[ord(char) - 96 for char in chars if char.islower()]
#[ord(char) - 38 for char in chars if char.isupper()]
#for val in values: total += val


# 4 simplify second loop w list comprehension
total = 0
chars = [list(set([char for char in line[:int(len(line)/2)] if char in line[int(len(line)/2):]]))[0] for line in input]
values = [ord(char) - 96 for char in chars if char.islower()]+[ord(char) - 38 for char in chars if char.isupper()]
for val in values: total += val
print(total)

# 5 use sum()
chars = [list(set([char for char in line[:int(len(line)/2)] if char in line[int(len(line)/2):]]))[0] for line in input]
total = sum([ord(char) - 96 for char in chars if char.islower()]+[ord(char) - 38 for char in chars if char.isupper()])
print(total)

# 6 sub chars into total
total = sum([ord(char) - 96 for char in [list(set([char for char in line[:int(len(line)/2)] if char in line[int(len(line)/2):]]))[0] for line in input] if char.islower()]+[ord(char) - 38 for char in [list(set([char for char in line[:int(len(line)/2)] if char in line[int(len(line)/2):]]))[0] for line in input] if char.isupper()])
print(total)

# 7 print directly
print(sum([ord(char) - 96 for char in [list(set([char for char in line[:int(len(line)/2)] if char in line[int(len(line)/2):]]))[0] for line in input] if char.islower()]+[ord(char) - 38 for char in [list(set([char for char in line[:int(len(line)/2)] if char in line[int(len(line)/2):]]))[0] for line in input] if char.isupper()]))

# 8 rearrange ord()
print(sum([char-96 for char in [ord(list(set([char for char in line[:int(len(line)/2)] if char in line[int(len(line)/2):]]))[0]) for line in input] if char >= 97]+[char-38 for char in [ord(list(set([char for char in line[:int(len(line)/2)] if char in line[int(len(line)/2):]]))[0]) for line in input] if char <= 90]))

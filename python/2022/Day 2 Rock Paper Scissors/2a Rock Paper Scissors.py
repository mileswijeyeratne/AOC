from rockPaperScissorsRawData import input

elf = {
    "A": 1,
    "B": 2,
    "C": 3
}

you = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

def find_total_score(x):
    total = 0
    for pair in x:
        elf_plays = elf[pair[0]]
        you_play = you[pair[1]]
        total += you_play
        if (you_play == 1 and elf_plays == 3) or (you_play == 2 and elf_plays == 1) or (you_play == 3 and elf_plays == 2):
            total += 6
        elif (you_play == 1 and elf_plays == 1) or (you_play == 2 and elf_plays == 2) or (you_play == 3 and elf_plays == 3):
            total += 3
        elif (you_play == 1 and elf_plays == 2) or (you_play == 2 and elf_plays == 3) or (you_play == 3 and elf_plays == 1):
            total += 0
    return total

print(find_total_score(input))
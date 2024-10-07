from rockPaperScissorsRawData import input

elf = {
    "A": 1,
    "B": 2,
    "C": 3
}

you = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

def find_total_score(x):
    total = 0
    for pair in x:
        elf_plays = elf[pair[0]]
        you_play = you[pair[1]]
        total += you_play
        if you_play == 0:
            should_play = (elf_plays + 2) % 3
            if should_play == 0:
                total += 3
            else: total += should_play
        elif you_play == 3:
            total += elf_plays
        elif you_play == 6:
            should_play = (elf_plays + 1) % 3
            if should_play == 0:
                total += 3
            else: total += should_play
    return total

print(find_total_score(input))
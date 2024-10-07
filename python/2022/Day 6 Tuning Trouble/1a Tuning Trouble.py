input = [line for line in open("Day 6 Tuning Trouble/rawData.txt", "r")][0]

def solve(x):
    
    used_chars = []

    for index, i in enumerate(x):
        print(used_chars)
        if i not in used_chars and len(used_chars) >= 4:
            print(f"{i} not in found")
            if len(used_chars) == len(set(used_chars)):
                return index
            del used_chars[0]
        elif len(used_chars) >= 4:
            del used_chars[0]
        used_chars.append(i)
        
    return

print(solve(input))
input = [line for line in open("rawData.txt", "r")][0]

def solve(x):
    
    used_chars = []

    for index, i in enumerate(x):
        print("\n",used_chars)
        if len(used_chars) >= 14:
            del used_chars[0]
        used_chars.append(i)
        if len(used_chars) >= 14 and len(used_chars) == len(set(used_chars)):
            return index + 1
        
    return

print(solve(input))
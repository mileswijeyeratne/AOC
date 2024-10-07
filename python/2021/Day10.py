from statistics import median

def _parse_data(data):
    return data.split("\n")


def solvePartA(data):
    data = _parse_data(data)
    openers = ["(", "[", "{", "<"]
    closers = [")", "]", "}", ">"]
    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
    res = 0
    for line in data:
        bracestack = []
        for char in line:
            if char in openers:
                bracestack.append(char)
            else:
                if not openers.index(bracestack.pop()) == closers.index(char):
                    res += scores[char]
                    break
    return res


def _remove_corrupted(data):
    openers = ["(", "[", "{", "<"]
    closers = [")", "]", "}", ">"]
    res = []
    for line in data:
        bracestack = []
        corrupted = False
        for char in line:
            if char in openers:
                bracestack.append(char)
            else:
                if not openers.index(bracestack.pop()) == closers.index(char):
                    corrupted = True
                    break
        if not corrupted:
            res.append(line)
    return res


def _score(braces):
    scores = {"(": 1, "[": 2, "{": 3, "<": 4}
    res = 0
    for b in braces:
        res *= 5
        res += scores[b]
    return res


def solvePartB(data):
    data = _parse_data(data)
    data = _remove_corrupted(data)

    openers = ["(", "[", "{", "<"]
    res = []
    for line in data:
        bracestack = []
        for char in line:
            if char in openers:
                bracestack.append(char)
            else:
                bracestack.pop()
        res.append(_score("".join(bracestack[::-1])))
    return median(sorted(res))


if __name__ == "__main__":
    test = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

    print(solvePartB(test))

def _parse_data(data):
    passports = []
    p = {}
    for line in data.replace(" ", "\n").split("\n") + [""]:
        if line == "":
            passports.append(p)
            p = {}
        else:
            field, data = line.split(":")
            p[field] = data

    return passports


def solvePartA(data):
    data = _parse_data(data)

    needed = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    res = 0

    for p in data:
        res += all([n in p.keys() for n in needed])

    return res


def solvePartB(data):
    data = _parse_data(data)

    needed = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    res = 0

    for p in data:
        if not (1920 <= int(p.get("byr", "0")) <= 2002):
            # print("byr")
            continue
        if not (2010 <= int(p.get("iyr", "0")) <= 2020):
            # print("iyr")
            continue
        if not (2020 <= int(p.get("eyr", "0")) <= 2030):
            # print("eyr")
            continue
        height = p.get("hgt", "00")
        if not height[-2:] in ["cm", "in"]:
            # print("hgt")
            continue
        if height[-2:] == "cm" and not (150 <= int(height[:-2]) <= 193):
            # print("hgt")
            continue
        if height[-2:] == "in" and not (59 <= int(height[:-2]) <= 76):
            # print("hgt")
            continue
        hcl = p.get("hcl", "zz")
        if not hcl[0] == "#" or not all([c in "1234567890abcdef" for c in hcl[1:]]) or len(hcl) != 7:
            # print("hcl")
            continue
        if not p.get("ecl", "") in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            # print("ecl")
            continue
        if not len(p.get("pid", "0")) == 9:
            # print("pid")
            continue
        res += 1

    return res


if __name__ == "__main__":
    test = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""

    print(solvePartB(test))

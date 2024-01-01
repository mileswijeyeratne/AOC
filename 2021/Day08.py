def _parse_data(data):
    data = data.split("\n")
    data = [d.split(" | ") for d in data]
    res = []
    for d in data:
        res.append([v.split(" ") for v in d])
    return res


def _str_minus_str(a, b):
    res = ""
    for item in a:
        if item not in b:
            res += item
    return res


def solvePartA(data):
    data = _parse_data(data)

    count = 0

    for record in data:
        for num in record[1]:
            match len(num):
                case 2 | 3 | 4 | 7:
                    count += 1

    return count


# god knows why i did this manually instead of brute-forcing it
def solvePartB(data):
    data = _parse_data(data)

    total = 0

    for record in data:
        nums = sorted(record[0], key=len)
        display = record[1]

        eight = nums[-1]
        one = nums[0]
        seven = nums[1]
        four = nums[2]

        nine = ""
        for num in nums[-4:-1]:
            c = _str_minus_str(eight, num)
            if _str_minus_str(c, four) == c:
                nine = num
                break

        six = ""
        zero = ""
        for num in [n for n in nums[-4:-1] if n != nine]:
            c = _str_minus_str(eight, num)
            if _str_minus_str(c, one) == c:
                zero = num
            else:
                six = num

        three = ""
        two = ""
        five = ""
        for num in nums[3:6]:
            c = _str_minus_str(eight, num)
            if _str_minus_str(c, one) == c:
                three = num
            else:
                if _str_minus_str(c, six) == "":
                    two = num
                else:
                    five = num

        nums = [zero, one, two, three, four, five, six, seven, eight, nine]
        for i, n in enumerate(nums):
            nums[i] = "".join(sorted(list(n), key=ord))

        display_num = 0
        for i, num in enumerate(display[::-1]):
            for j, n in enumerate(nums):
                if "".join(sorted(list(num))) == n:
                    display_num += j * 10**i

        total += display_num

    return total


if __name__ == "__main__":
    test = """acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"""

    print(solvePartB(test))

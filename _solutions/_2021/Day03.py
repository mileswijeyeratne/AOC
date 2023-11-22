def _parse_data(data):
    data = [list(n) for n in data.split("\n")]
    return data


def _get_most_common(data, i):
    ones = zeros = 0
    for d in data:
        match d[i]:
            case "1":
                ones += 1
            case "0":
                zeros += 1

    return "1" if ones >= zeros else "0"


def solvePartA(data):
    data = _parse_data(data)

    epsilon = gamma = ""

    for i in range(len(data[0])):
        d = _get_most_common(data, i)
        epsilon += d
        gamma += "0" if d == "1" else "1"

    return int(epsilon, 2) * int(gamma, 2)


def _o2_filter(data, i):
    d = _get_most_common(data, i)

    return list(filter(lambda x: x[i] == d, data))


def _co2_filter(data, i):
    d = _get_most_common(data, i)

    return list(filter(lambda x: x[i] != d, data))


def solvePartB(data):
    data = _parse_data(data)

    o2_data = data.copy()
    i = 0
    while len(o2_data) > 1:
        o2_data = _o2_filter(o2_data, i)
        i += 1

    co2_data = data.copy()
    i = 0
    while len(co2_data) > 1:
        co2_data = _co2_filter(co2_data, i)
        i += 1

    o2 = int("".join(o2_data[0]), 2)
    co2 = int("".join(co2_data[0]), 2)

    return o2 * co2


if __name__ == "__main__":
    test = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

    print(solvePartB(test))

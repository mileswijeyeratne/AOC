def _parse_data(data):
    data = [i.split(" ") for i in data.split("\n")]
    data = [(d[0], int(d[1])) for d in data]
    return data

def solvePartA(data):
    data = _parse_data(data)

    x = y = 0

    for move, dist in data:
        match move:
            case "forward":
                x += dist
            case "up":
                y -= dist
            case "down":
                y += dist

    return x*y

def solvePartB(data):
    data = _parse_data(data)

    a = x = y = 0

    for move, val in data:
        match move:
            case "forward":
                x += val
                y += a*val
            case "up":
                a -= val
            case "down":
                a += val

    return x * y

if __name__ == "__main__":
    test = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

    print(solvePartB(test))
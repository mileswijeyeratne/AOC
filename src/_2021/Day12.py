from collections import Counter

def _parse_data(data):
    conns = [conn.split("-") for conn in data.split("\n")]
    res = {}
    for s, e in conns:
        if e != "start":
            if s in res.keys():
                res[s].append(e)
            else:
                res[s] = [e]
        if s != "start":
            if e in res.keys():
                res[e].append(s)
            else:
                res[e] = [s]
    return res

def _search(path, caves, valid_func):
    if path[-1] == "end":
        return 1
    res = 0
    for c in caves[path[-1]]:
        if valid_func(path, c):
            p = path.copy() + [c]
            res += _search(p, caves, valid_func)
    return res

def _check_valid_a(path, tunnel):
    return not (tunnel.islower() and tunnel in path)

def _check_valid_b(path, tunnel):
    c = Counter(path)
    in_path = tunnel in path and tunnel.islower()
    for t, i in c.items():
        if t.islower() and i == 2 and in_path:
            return False
    return True


def solvePartA(data):
    data = _parse_data(data)

    p = ["start"]

    return _search(p, data, _check_valid_b)

def solvePartB(data):
    data = _parse_data(data)

    p = ["start"]

    return _search(p, data, _check_valid_b)


if __name__ == "__main__":
    test = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

    print(solvePartB(test))

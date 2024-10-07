def _parse_data(data):
    return [eval(line) for line in data.split("\n")]

def _add(a, b):
    return [a, b]

def _reduce(pair):
    

def solvePartA(data):
    data = _parse_data(data)



def solvePartB(data):
    pass

if __name__ == "__main__":
    test = """[1,2]
[[1,2],3]
[9,[8,7]]
[[1,9],[8,5]]
[[[[1,2],[3,4]],[[5,6],[7,8]]],9]
[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]
[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]
"""

    print(solvePartA(test))

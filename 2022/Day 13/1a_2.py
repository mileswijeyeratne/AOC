data = [line.strip() for line in open("Day 13/rawData.txt")]

input = []
tuple_to_add = []
for line in data:
    if line == "":
        input.append((tuple_to_add[0], tuple_to_add[1]))
        tuple_to_add = []
    else: tuple_to_add.append(eval(line))
if tuple_to_add != []: input.append((tuple_to_add[0], tuple_to_add[1]))

input_test = [
    ([1,1,3,1,1], [1,1,5,1,1]),
    ([[1],[2,3,4]], [[1],4]),
    ([9], [[8,7,6]]),
    ([[4,4],4,4], [[4,4],4,4,4]),
    ([7,7,7,7], [7,7,7]),
    ([], [3]),
    ([[[]]], [[]]),
    ([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9])
]


def compare(pair):
    left, right = pair
    for index, item in enumerate(left):
        if 
#from data import input

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

def compare_pair(pair):
    left = pair[0]
    right = pair[1]

    for index, item in enumerate(left):
        try:
            if type(item) == list and type(right[index]) == list:
                return compare_pair((item, right[index]))
            elif type(item) == int and type(right[index]) == int:
                if item > right[index]:
                    return False
                elif item < right[index]:
                    return True
            elif type(item) != type(right[index]):
                if type(item) != list: returned = compare_pair(([item], right[index]))
                else:  return compare_pair((item, [right[index]]))
        except IndexError:
            return False
    return True


running_sum = 0
for index, pair in enumerate(input_test):
    if compare_pair(pair):
        running_sum += index+1

print(running_sum)

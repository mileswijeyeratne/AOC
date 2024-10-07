"""
https://adventofcode.com/2022/day/20
"""

TESTDATA = """1
2
-3
3
-2
0
4"""

class CircularList:
    """
    Scuffed class to enable lists to loop aound
    should probably inherit from list and modify dunder methods rather than have a reference to a list called self.contents
    """
    __slots__ = ["contents"]

    def __init__(self, contents: list) -> None:
        self.contents = contents
    
    def shift(self, index, amount):
        target = (index + amount) % (len(self.contents)-1)
        temp = self.contents.pop(index)
        self.contents.insert(target, temp)

    def after_0(self, index):
        index_of_0 = self.contents.index(0)
        return self.contents[(index + index_of_0) % len(self.contents)]
    
    def index(self, index):
        return self.contents.index(index)
    
    def __getitem__(self, key):
        return self.contents[key]

    def __len__(self):
        return len(self.contents)

    def __str__(self):
        return str(self.contents)

def _parse_data(data):
    return CircularList([int(i) for i in data.split("\n")])

def _mix(order, data):
    counter = 0
    l = len(data)

    while counter < l:
        index = order.index(counter)
        val = data[index]
        order.shift(index, val)
        data.shift(index, val)
        counter += 1

def A(data):
    data = _parse_data(data)
    order = CircularList([i for i in range(len(data))])

    _mix(order, data)

    return data.after_0(1000) + data.after_0(2000) + data.after_0(3000)


def B(data):
    data = _parse_data(data)
    order = CircularList([i for i in range(len(data))])

    data.contents = [i*811589153 for i in data.contents]

    for _ in range(10): _mix(order, data)
    
    return data.after_0(1000) + data.after_0(2000) + data.after_0(3000)


if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run AOC day 20")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    input_data = TESTDATA if args.t else aocd.get_data(
        session="53616c7465645f5f6a8cadc93b9182aac8706b0eaa2c354155a2097c65ae98ce052bb1a6d2f55bc96f4b164422ad0e9fdd7b28dadeb8e47a29204fa7d603cbaf",
        day=20,
        year=2022)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print("Program finished in", time_taken, "seconds")
    print(res)
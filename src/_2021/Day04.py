class _Board:
    def __init__(self, data):
        self.rows = [[0 for _ in range(5)] for _ in range(5)]
        self.guessed_rows = [[False for _ in range(5)] for _ in range(5)]
        self.guessed_cols = [[False for _ in range(5)] for _ in range(5)]
        # self.guessed_diag_0 = [False] * 5
        # self.guessed_diag_1 = [False] * 5

        self._fill(data)

    def __str__(self):
        return self.rows.__str__()

    def _fill(self, data):
        data = data.split(" ")
        for i, d in enumerate(data):
            ci, ri = divmod(i, 5)
            self.rows[ci][ri] = int(d)

    def guess(self, num):
        for ri, row in enumerate(self.rows):
            for ci, cell in enumerate(row):
                if cell == num:
                    self.guessed_rows[ri][ci] = True
                    self.guessed_cols[ci][ri] = True
                    # if ci == ri: self.guessed_diag_0[ci] = True
                    # if ci + ri == 4: self.guessed_diag_1[ci] = True

                    if self.has_won(): return self.get_score(num)

    def has_won(self):
        for row in self.guessed_rows:
            if row == [True] * 5:
                return True
        for col in self.guessed_cols:
            if col == [True] * 5:
                return True
        # if self.guessed_diag_0 == [True] * 5:
        #     return True
        # if self.guessed_diag_1 == [True] * 5:
        #     return True

    def get_score(self, last_called):
        sum = 0
        for ri, row in enumerate(self.guessed_rows):
            for ci, cell in enumerate(row):
                if cell == False: sum += self.rows[ri][ci]

        return sum * last_called


def _parse_data(data):
    data = data.split("\n") + [""]
    nums = data.pop(0).split(",")
    boards = []
    b = []
    for row in data[1:]:
        if row == "":
            boards.append(" ".join(b).replace("  ", " ").lstrip(" "))
            b = []
        else:
            b.append(row)

    boards = [_Board(data) for data in boards]
    nums = [int(num) for num in nums]

    return nums, boards


def solvePartA(data):
    nums, boards = _parse_data(data)

    #print(nums)
    #for b in boards: print(b)

    for n in nums:
        for b in boards:
            g = b.guess(n)
            if g is not None:
                return g

    return "No solutions"


def solvePartB(data):
    nums, boards = _parse_data(data)

    print(nums)
    for b in boards: print(b)

    for n in nums:
        b_to_del = None
        s = 0
        for i, b in enumerate(boards):
            g = b.guess(n)
            if g is not None:
                b_to_del = i
                s = g
        if b_to_del is not None:
            if len(boards) > 1:
                boards.pop(b_to_del)
            else:
                return s


if __name__ == "__main__":
    test = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

    print(solvePartB(test))

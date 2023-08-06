import _2021
import _2022

_solutions = {
    2021: {
        1: (_2021.Day01.solvePartA, _2021.Day01.solvePartB),
        2: (_2021.Day02.solvePartA, _2021.Day02.solvePartB),
        3: (_2021.Day03.solvePartA, _2021.Day03.solvePartB),
        4: (_2021.Day04.solvePartA, _2021.Day04.solvePartB),
        5: (_2021.Day05.solvePartA, _2021.Day05.solvePartB),
        6: (_2021.Day06.solvePartA, _2021.Day06.solvePartB),
        7: (_2021.Day07.solvePartA, _2021.Day07.solvePartB),
        8: (_2021.Day08.solvePartA, _2021.Day08.solvePartB),
        9: (_2021.Day09.solvePartA, _2021.Day09.solvePartB),
        10: (_2021.Day10.solvePartA, _2021.Day10.solvePartB),
        11: (_2021.Day11.solvePartA, _2021.Day11.solvePartB),
        12: (_2021.Day12.solvePartA, _2021.Day12.solvePartB),
        13: (_2021.Day13.solvePartA, _2021.Day13.solvePartB),
        14: (_2021.Day14.solvePartA, _2021.Day14.solvePartB),
        15: (_2021.Day15.solvePartA, _2021.Day15.solvePartB),
    },

    2022: {
        13: (_2022.Day13.solvePartA, _2022.Day13.solvePartB),
    },
}

class Solution:
    def __init__(self, year, day):
        self.solutions = _solutions[year][day]

    def solvePartA(self, data):
        return self.solutions[0](data)

    def solvePartB(self, data):
        return self.solutions[1](data)

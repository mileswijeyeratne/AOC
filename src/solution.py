import _2021

_solutions = {
    2021: [
        (_2021.Day01.solvePartA, _2021.Day01.solvePartB),
        (_2021.Day02.solvePartA, _2021.Day02.solvePartB),
        (_2021.Day03.solvePartA, _2021.Day03.solvePartB),
        (_2021.Day04.solvePartA, _2021.Day04.solvePartB),
        (_2021.Day05.solvePartA, _2021.Day05.solvePartB),
        (_2021.Day06.solvePartA, _2021.Day06.solvePartB),
        (_2021.Day07.solvePartA, _2021.Day07.solvePartB),
        (_2021.Day08.solvePartA, _2021.Day08.solvePartB),
    ],
}

class Solution:
    def __init__(self, year, day):
        self.solutions = _solutions[year][day-1]

    def solvePartA(self, data):
        return self.solutions[0](data)

    def solvePartB(self, data):
        return self.solutions[1](data)

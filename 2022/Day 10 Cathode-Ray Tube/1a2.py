class Solver():
    def __init__(self) -> None:
        self.input = [line.strip().split(" ") for line in open("Day 10/rawData.txt")]
        self.cycles = 1
        self.xvalue = 1
        self.total_sum = 0
        self.done = False
        self.current_processing = []
    
    def check_special(self):
        values_to_check = [20, 60, 100, 140, 180, 220]
        if self.cycles in values_to_check:
            self.total_sum += self.xvalue * self.cycles
    
    def check_done(self):
        if self.cycles >= 220:
            self.done = True
    
    def solve(self):
        for line in self.input:
            if line[0] == "addx":
                self.current_processing = line
            self.cycles += 1
            self.check_special()
            self.check_done()
            if self.current_processing != []:
                self.cycles += 1
                self.xvalue += int(self.current_processing[1])
                self.current_processing = []
                self.check_special()
                self.check_done()
            if self.done:
                return self.total_sum

            


solver = Solver()
print(solver.solve())
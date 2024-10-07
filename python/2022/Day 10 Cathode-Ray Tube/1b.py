class Solver():
    def __init__(self) -> None:
        self.input = []
        for line in open("rawData.txt"):
            l = line.strip().split(" ")
            if l[0] == "addx":
                self.input.append(["noop"])
            self.input.append(l)
        self.cycles = 0
        self.xvalue = 1
        self.display = []
        for i in range(6):
            row = []
            for i in range(40): row.append(".")
            self.display.append(row)
    
    def tick_display(self):
        row_to_change = self.cycles // 40
        index_to_change = self.cycles % 40
        if self.xvalue - index_to_change < 2 and self.xvalue - index_to_change > -2:
            self.display[row_to_change][index_to_change] = "#"

    def solve(self):
        for line in self.input:
            self.tick_display()
            if line[0] == "addx":
                self.xvalue += int(line[1])
            self.cycles += 1
        return self.display
    
solver = Solver()
display = solver.solve()
for row in display:
            row_to_print = ""
            for char in row:
                row_to_print = row_to_print + char
            print(row_to_print)

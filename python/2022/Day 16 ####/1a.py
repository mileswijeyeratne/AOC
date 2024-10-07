data = [line.strip().split(";") for line in open("Day 16/rawData.txt")]

input = {}
for line in data:
    line_to_append = (line[0].split("=")[1], line[1][24:].split(", "))
    input[line[0][6:8]] = line_to_append


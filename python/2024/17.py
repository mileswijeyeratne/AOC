"""
https://adventofcode.com/2024/day/17

      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 17   00:31:14   2162      0       >24h  15747      0

Honestly quite a fun day even if I just wans't thinking straight.
Part a took way too long bc I didn't read the question right I completely
overlooked combo operands and just made silly mistakes
part b was quite fun, I originally thought of doing a bfs solving backwards but
thought that the branch instruction would make it impossible with loops so just
tried messing around with numbers. Found some patterns to do with it base - 8
but nothing more then that.
finally went back to the dfs approach and after sorting out a bug that i still
dont understand why its wrong, completed it.
"""

TESTDATA = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""


def _parse_data(data):
    registers, program = data.split("\n\n")
    registers = list(map(int, [line[12:]
                     for line in registers.split("\n")]))
    program = list(map(int, program[9:].split(",")))

    return registers, program


def get_combo(registers, operand):
    if operand < 4:
        return operand
    return registers[operand - 4]


def execute(registers, opcode, operand):
    res = -1

    def div(operand):
        return registers[0] >> get_combo(registers, operand)

    if opcode == 0:  # div
        registers[0] = div(operand)

    if opcode == 1:  # xor
        registers[1] = registers[1] ^ operand

    if opcode == 2:  # mod 8
        registers[1] = get_combo(registers, operand) % 8

    if opcode == 3:  # njz
        if registers[0] != 0:
            return operand, res

    if opcode == 4:  # xor b c
        registers[1] = registers[1] ^ registers[2]

    if opcode == 5:  # out
        res = get_combo(registers, operand) % 8

    if opcode == 6:  # div b
        registers[1] = div(operand)

    if opcode == 7:  # div c
        registers[2] = div(operand)

    return -1, res


def run(registers, program):
    res = []

    i = 0
    while i < len(program):
        opcode = program[i]
        operand = program[i+1]

        ip, out = execute(registers, opcode, operand)

        if out != -1:
            res.append(out)

        if ip == -1:
            i += 2
        else:
            i = ip

    return res


def A(data):
    return ",".join(map(str, run(*_parse_data(data))))


def _B(data):
    # trial and error finding patterns - didn't manage to finish in the morning
    # so took a step back
    (_, b, c), program = _parse_data(data)

    a = 35184372882080
    last = 0

    while True:
        res = run([a, b, c], program)
        if res == program:
            return a
        if res[:7] == program[:7]:
            # print("#")
            # print(a)
            # print(a - last)
            print(a, oct(a - last))
            last = a
        # if len(res) == len(program):
        #     # 35184372088832
        #     print(a)
        #     break
        a += int(0o10000000)

    return -1


def B(data):
    (_, b, c), program = _parse_data(data)

    def dfs(a, solved):
        for i in range(2**3):  # mod 8
            next = (a << 3) + i
            res = run([next, b, c], program)
            if res == program:
                return next
            if solved < 0:
                # i still dont understand why this isnt '==' or '<='
                return -1
            if res == program[solved:] and (v := dfs(next, solved-1)) != -1:
                # garunteeded to be min as we count up
                return v
        return -1

    return dfs(0, len(program) - 1)


if __name__ == "__main__":
    import aocd
    from time import time
    from argparse import ArgumentParser
    import os
    parser = ArgumentParser(description="Run AOC day 1")
    parser.add_argument("part", choices=["a", "b"], help="The part runs")
    parser.add_argument("-t", action="store_true", help="Runs on test data")
    args = parser.parse_args()

    session = os.environ.get("aoc-session")
    assert session is not None, "Please set 'aoc-session' environment variable"

    input_data = TESTDATA if args.t else aocd.get_data(
        session=session,
        day=17,
        year=2024)
    part = A if args.part == "a" else B

    time_start = time()
    res = part(input_data)
    time_taken = time() - time_start

    print(f"Program finished in {time_taken * 1000:.1f} ms")
    print(res)

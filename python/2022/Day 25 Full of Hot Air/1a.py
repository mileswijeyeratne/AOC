def digit_add(digits_to_add):
    digits = {
        "2": 2,
        "1": 1,
        "0": 0,
        "-": -1,
        "=": -2
    }
    total = sum([digits[digit] for digit in digits_to_add])
    carry = 0
    if total > 2:
        carry = 1
        total -= 5
    elif total < -2:
        carry = -1
        total += 5
    total = [k for k, v in digits.items() if v == total][0]
    carry = [k for k, v in digits.items() if v == carry][0]
    return total, carry

def number_add(num1_inp, num2_inp):
    num1 = num1_inp[::-1]
    num2 = num2_inp[::-1]
    max_len = max(len(num1), len(num2))
    while len(num1) < max_len: num1 = num1 + "0"
    while len(num2) < max_len: num2 = num2 + "0"

    carry = "0"
    answer = ""
    for char_index in range(max_len):
        digit, carry = digit_add([num1[char_index], num2[char_index], carry])
        answer = answer + digit
    answer = answer + carry
    return answer.rstrip("0")[::-1]

data = [line.strip() for line in open("Day 25/rawData.txt")]

total = "0"
for line in data:
    total = number_add(total, line)

print(total)
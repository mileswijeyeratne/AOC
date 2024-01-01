data = [line.strip() for line in open("Day 20/rawData", "r")]

result = ["#" for _ in range(len(data))]

# orginise new list
for char in data:
    first_placeholder = result.index("#")
    input_index = first_placeholder + int(char)
    if input_index < 0:
        result.insert(-abs(input_index)%len(result) - abs(input_index)//len(result), char)
    elif input_index < first_placeholder:
        result.insert(input_index, char)
    elif len(result) > input_index:
        result.insert(input_index + 1, char)
    elif len(result) <= input_index:
        result.insert((input_index % len(result)) + (input_index//len(result)), char)
    result.remove("#")


#find at char 1000, 2000, 3000
char_at_1000 = result[(result.index("0") + 1000) % len(result)]
char_at_2000 = result[(result.index("0") + 2000) % len(result)]
char_at_3000 = result[(result.index("0") + 3000) % len(result)]

print(char_at_1000, char_at_2000, char_at_3000)
print(int(char_at_1000) + int(char_at_2000) + int(char_at_3000))
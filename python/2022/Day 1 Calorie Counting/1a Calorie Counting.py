from calorieCountingRawData import input


def find_most_calories(x):
    current_total = 0
    current_hieghest = 0
    for i in x:
        if i is None:
            if current_total > current_hieghest:
                current_hieghest = current_total
            current_total = 0
        else:
            current_total += i
    return current_hieghest


print(find_most_calories(input))

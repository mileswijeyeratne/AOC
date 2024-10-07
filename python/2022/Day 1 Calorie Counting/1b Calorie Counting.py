from calorieCountingRawData import input


def find_most_calories(x):
    current_total = 0
    current_one = 0
    current_two = 0
    current_three = 0
    for i in x:
        print(i)
        print(current_total)
        if i is None:
            if current_total > current_one:
                current_three = current_two
                current_two = current_one
                current_one = current_total
            elif current_total > current_two:
                current_three = current_two
                current_two = current_total
            elif current_total > current_three:
                current_three = current_total
            current_total = 0
        else:
            current_total += i
    print(current_one, current_two, current_three)
    return current_one + current_two + current_three

y = [3344,8938,7923,3979,2753,5730,4225,None,24216,7432,18284,None,3475,9177,6769,11335,8061,9302,8132]
print(find_most_calories(input))

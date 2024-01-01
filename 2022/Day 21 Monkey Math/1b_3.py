from sympy import symbols, solve
x = symbols('x')

data = {}
f = open("Day 21/rawData.txt", "r")
for line in f:
    data[line.strip()[:4]] = line.strip()[6:] 
f.close()

def update(str_to_check):
    special_chars = ["/", "*", "-", "+", " ", "(", ")", "!"]

    for index, char in enumerate(str_to_check):
        if not char.isnumeric() and not char in special_chars:
            return str_to_check[:index] + "(" + data[str_to_check[index:index+4]] + ")" + str_to_check[index+4:]

    return str_to_check    
        

def eval_key(key):
    string_to_eval = str(data[key])
    last_cycle = ""

    while last_cycle != string_to_eval:
        last_cycle = string_to_eval
        string_to_eval = update(string_to_eval)
    
    return string_to_eval

result = eval_key("sdgh") + " = " + eval_key("cdvj")



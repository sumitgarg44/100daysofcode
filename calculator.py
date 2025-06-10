from static.arts import calc

def add (n1, n2):
    return n1 + n2

def subtract (n1, n2):
    return n1 - n2

def multiply (n1, n2):
    return n1 * n2

def divide (n1, n2):
    return n1 / n2

def calculator():
    print(calc.logo)
    f_num = float(input("What's the first number?: "))
    operation = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    for symbol in operation:
        print(symbol)

    continue_loop = True

    while continue_loop:
        operation_symbol = input("Pick an operation from above: ")
        n_num = float(input("What's the next number?: "))
        calculation_function = operation[operation_symbol]
        answer = calculation_function(f_num, n_num)
        print (f"{f_num} {operation_symbol} {n_num} = {answer}")
        is_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation.: ")

        if is_continue == "y":
            f_num = answer
        else:
            continue_loop = False
            calculator()

calculator()

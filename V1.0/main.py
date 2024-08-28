from art import logo

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations_dict = {
"+" : add,
"-": subtract,
"*": multiply,
"/": divide,
}

def calculator():
    continue_calculating = True
    print(logo)
    first_number = float(input("What's the first number?: "))
    while continue_calculating == True:

        for symbol in operations_dict:
            print(symbol)

        operation = input("Pick an operation: ")

        second_number= float(input("What's the next number?: "))
        result = operations_dict[operation](first_number, second_number)

        print(f"{first_number} {operation} {second_number} = {result}.")
        keep_number = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation").lower()

        if keep_number == "y":
            first_number = result
        else:
            continue_calculating = False
            print("\n" * 20)
            calculator()
calculator()

#Method 2: I prefered doing it this way, but for the same of learning and practicing dictionaries I did it Angela's way using recursion

# from art import logo
#
# symbols = """
# +
# -
# *
# /
# """
#
#
# def add(n1, n2):
#     return n1 + n2
#
#
# def subtract(n1, n2):
#     return n1 - n2
#
#
# def multiply(n1, n2):
#     return n1 * n2
#
#
# def divide(n1, n2):
#     return n1 / n2
#
#
# def calculate(num1, num2, symbol):
#     if symbol == "+":
#         return add(num1, num2)
#     elif symbol == "-":
#         return subtract(num1, num2)
#     elif symbol == "*":
#         return multiply(num1, num2)
#     elif symbol == "/":
#         return divide(num1, num2)
#
#
# continue_calculating = True
# print(logo)
# while continue_calculating == True:
#     first_number = float(input("What's the first number?: "))
#     print(symbols)
#     operation = input("Pick an operation: ")
#     second_number = float(input("What's the next number?: "))
#     result = calculate(first_number, second_number, operation)
#     print(f"{first_number} {operation} {second_number} = {result}.")
#     keep_number = input(
#         f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation").lower()
#
#     while keep_number == "y":
#         first_number = result
#         print(symbols)
#         operation = input("Pick an operation: ")
#         second_number = float(input("What's the next number?: "))
#         result = calculate(first_number, second_number, operation)
#         print(f"{first_number} {operation} {second_number} = {result}.")
#         keep_number = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation").lower()

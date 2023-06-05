import sys

def add(a, b):

    return a + b

def subtract(a, b):

    return a - b

def multiply(a, b):

    return a * b

def divide(a, b):

    return a / b

def main():

    function_map = {

        '+': add,

        '-': subtract,

        '*': multiply,

        '/': divide

    }

    

    if len(sys.argv) != 4:

        print('Usage: basic_calculator.py <operand1> <operator> <operand2>')

        sys.exit(1)

        

    try:

        operand1 = int(sys.argv[1])

        operand2 = int(sys.argv[3])

        operator = sys.argv[2]

    except ValueError:

        print('Error: Invalid operands')

        sys.exit(1)

    

    if operator not in function_map:

        print('Error: Invalid operator')

        sys.exit(1)

        

    result = function_map[operator](operand1, operand2)

    print(result)

if __name__ == '__main__':

    main()

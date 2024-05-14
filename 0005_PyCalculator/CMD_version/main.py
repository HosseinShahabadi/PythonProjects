import os

logo = '''
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
'''

os.system('cls' if os.name == 'nt' else 'clear')
print(logo)

def is_float(element: any):
    '''Check if an element is float'''
    if element is None: 
        return False
    try:
        float(element)
        return True
    except ValueError:
        return False

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def divide(num1, num2):
    return num1 / num2

def multiply(num1, num2):
    return num1 * num2

def power(num1, num2):
    return num1 ** num2

def calculator():
    # Get & validate user data for the first number.
    num1 = input("What's the first number: ")
    while not is_float(num1):
        num1 = input("Wrong input, What's the first number: ")
    num1 = float(num1)

    while 1:
        # Get & validate user data for the operation.
        operation = input("Pick an operation: ")
        while operators.get(operation) == None:
            operation = input("Wrong input, Pick an operation: ")

        # Get & validate user data for the second number.
        num2 = input("What's the second number: ")
        while not is_float(num2):
            num2 = input("Wrong input, What's the second number: ")
        num2 = float(num2)

        # Calculating
        func = operators[operation][0]
        answer = func(num1, num2)

        print(f"{num1} {operation} {num2} = {answer}")

        user_choice = input(f"Type 'y' to continue with {answer}, 'r' to restart, or 'n' to exit: ").lower()
        if user_choice == 'y':
            num1 = answer
        elif user_choice == 'r':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(logo)
            calculator()
            break
        else:
            break

operators = {
    "+": [add, 'add'],
    "-": [subtract, 'subtract'],
    "/": [divide, 'divide'],
    "*": [multiply, 'multiply'],
    "**": [power, 'power'],
}

print("Supported operations:")
for opt in operators:
    print(f"{opt}: {operators[opt][1]}")

calculator()

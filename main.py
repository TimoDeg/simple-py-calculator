def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def division(a, b):
    return a / b

def multiplication(a, b):
    return a * b


def calculator():
    """Main calculator logic handling user input and operation choice."""
    print("Simple Calculator")
    print("Operations: + - * /")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operation:")
    result = 0

    match op:
        case "+":
            result = addition(a, b)
        case "-":
            result = subtraction(a, b)
        case "/":
            result = division(a, b)
        case "*":
            result = multiplication(a, b)
        case _:
            return "Error. False input."
    
    return f"The result is: {result}"


if __name__ == "__main__":
    try:
        print(calculator())
    except Exception as e:
        print(f"Error: {e}")
    
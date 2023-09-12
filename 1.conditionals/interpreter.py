def interpret_math_expression(expression):
    # Cleanup expression
    expression = expression.strip()

    # Parse operator and operands
    values = expression.split(' ')

    # Expected format: x operator y
    x = float(values[0])
    operator = values[1]
    y = float(values[2])

    # Perform operation
    match operator:
        case '+':
            return x + y
        case '-':
            return x - y
        case '*':
            return x * y
        case '/':
            return x / y
        case _:
            # Invalid operator
            return None


def main():
    # Prompt for math expression
    expression = input('What is the math expression? ')
    result = interpret_math_expression(expression)

    # Float with only 1 decimal place
    print(f'The result is {round(result, 1)}')


main()

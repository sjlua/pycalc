def compute(expression):
    """Compute a simple arithmetic expression."""
    num0, operator, num1 = expression.split(' ')
    num0 = float(num0)
    num1 = int(num1)

    if operator == '+':
        return num0 + num1
    elif operator == '-':
        return num0 - num1
    elif operator == '*':
        return num0 * num1
    elif operator == '/':
        return num0 / num1
    else:
        print('unknown operator!')
        return None

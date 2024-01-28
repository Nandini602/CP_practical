def diffWaysToCompute(expression):
    if "-" not in expression and "+" not in expression and "*" not in expression:
        return [int(expression)]

    result = []
    for i in range(len(expression)):
        if expression[i] in ['+', '-', '*']:
            left_results = diffWaysToCompute(expression[:i])
            right_results = diffWaysToCompute(expression[i+1:])

            for left in left_results:
                for right in right_results:
                    if expression[i] == '+':
                        result.append(left + right)
                    elif expression[i] == '-':
                        result.append(left - right)
                    elif expression[i] == '*':
                        result.append(left * right)

    return result

# Example usage:
expression = "2*3-4*5"
print(diffWaysToCompute(expression))

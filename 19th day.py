def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):  
            stack.append(int(token))
        else:
            
            b = stack.pop()
            a = stack.pop()
            
            
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b)) 
            elif token == '^':
                stack.append(a ** b)  
    
    return stack.pop()

expression = "3 4 2 * 1 5 - 2 3 ^ ^ / +"
print("The result of the postfix expression is:", evaluate_postfix(expression))

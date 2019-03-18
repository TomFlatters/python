# create a function that converts from an infix notation to a reverse polish notation (with a stack):

# e.g. " d - ((a + b) * c) " --> " [ a, b, +, c, *, d, - ] "

def convertExpression(expression):
    stack_ex = []

    if "(" in expression: 
        first = expression.rfind("(")
        stack_ex.append(expression[first+1]) # add the element after the last bracket
        for i in expression[first+1:] not ")":

# to be continued (there are more steps than one would initially assume)

# plan: 
# 1. rewrite expression without brackets
# 2. add expressions to numerical and operational stack
# 3. combine the stacks
# 4. return combined stacks



    return stack_ex
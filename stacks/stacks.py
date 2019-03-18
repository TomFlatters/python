# " a stack is a list with just two operations: push and pop "

# define a stack as an empty list:
stack = []

# push to the stack:
stack.append(10)
stack.append(20)

# retrieve the 'top' item:
x = stack.pop()
print("Popped result is: ", x)
print("Stack is: ", stack)

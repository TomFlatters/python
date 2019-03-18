# a simple programming language using stacks:

def tomlanguage(instructions):
    stack = []
    for inst in instructions:
        if inst == "+":
            x = stack.pop()
            y = stack.pop()
            stack.append(x + y)
        elif inst == "-":
            x = stack.pop()
            y = stack.pop()
            stack.append(x-y)
        elif inst == "*":
            x = stack.pop()
            y = stack.pop()
            stack.append(x*y)
        elif inst == "/":
            x = stack.pop()
            y = stack.pop()
            stack.append(x/y)
        else:
            stack.append(inst)
    return stack[0]

# print(tomlanguage([ 1, 2, 3, 4, "+", "+", "-" ])) #8
# print(tomlanguage([ 1, 2, 3, 4, "*", "*", "*"])) #24
# print(tomlanguage([ 2, 2, 3, 4, "*", "/", "/"])) #3.0 ( because of division )


def calculate(s):
    stack = []
    num = 0
    last_op = '+'
    s = s.replace(' ', '') + '+'
    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        else:
            if last_op == '+':
                stack.append(num)
            elif last_op == '-':
                stack.append(-num)
            elif last_op == '*':
                stack.append(stack.pop() * num)
            elif last_op == '/':
                top = stack.pop()
                if top < 0:
                    stack.append(-(-top // num))
                else:
                    stack.append(top // num)
            last_op = char
            num = 0
    return sum(stack)
print(calculate("14-3/2"))

def basic_cal(s):
    eq = ""
    for i in s:
        if i != " ":
            eq += i
    num = 0
    for i in eq:
        if i.isdigit():
            num = num * 10 + i
        else:
            if i == "*" or i == "/":
                sym = i
                num2 = 0
                while i.isdigit():
                    num2 = num2 * 10 + i
                if sym == "*":
                    num = num * num2
                else:
                    num = num / num2


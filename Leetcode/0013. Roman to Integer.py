def roman_to_int(s):
    s_new = []
    sum = 0
    for i in range(0, len(s)):
        if s[i] == "M":
            s_new.append(1000)
        elif s[i] == "D":
            s_new.append(500)
        elif s[i] == "C":
            s_new.append(100)
        elif s[i] == "L":
            s_new.append(50)
        elif s[i] == "X":
            s_new.append(10)
        elif s[i] == "V":
            s_new.append(5)
        elif s[i] == "I":
            s_new.append(1)
    n = 0
    for i in range(0, len(s_new) - 1):
        if s_new[i + 1] > s_new[i]:
            sum += s_new[i + 1] - s_new[i]
            n = 1
        else:
            sum += s_new[i]
    if n == 1:
        return sum
    else:
        return sum + s_new[len(s_new) - 1]

print(roman_to_int("MCMXCIV"))
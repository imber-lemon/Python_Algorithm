def gen_bin(lenght, sys, num = ""):
    if lenght == 0:
        print(num)
        return
    for i in range(sys):
        gen_bin(lenght - 1, sys, num + str(i))
gen_bin(5, 5)

lst = [i for i in open(r"C:\Users\Mityukov_N\17.txt")]
print(lst)
not_max = []
maxi = 0
while maxi % 100 != 28:
    maxi = max(lst)
    if maxi % 100 != 28:
        not_max.append(maxi)

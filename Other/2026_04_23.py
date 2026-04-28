lst = [int(i) for i in open("17.txt")]
print(lst)
not_maxi = []
maxi = 0
while maxi % 100 != 28:
    maxi = max(list(set(lst) - set(not_maxi)))
    if maxi % 100 != 28:
        not_maxi.append(maxi)
# for i in range(0, len(lst), 3):
#     for x in range()
print(maxi)

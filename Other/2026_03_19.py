def matches(players):
    d = dict()
    pl1 = players[0:len(players)//2]
    pl2 = players[len(players)//2:]
    for i in range(len(pl1) * 2 - 1):
        print(i + 1, "тур:")
        # pl2.insert(0, pl2[-1])
        # pl2.pop(-1)

        pl1.insert(1, pl2[0]), pl2.append(pl1[-1])
        pl2.pop(0)
        pl1.pop(-1)
        # for j in range(len(pl1)):
        #     print(pl1[j], "играет с", pl2[j])
        # print('                                     ')
        for j in range(len(pl2)):
            if pl1[j] not in d:
                d[pl1] = []
            if pl2[j] not in d:
                d[pl2] = []
            d[pl1[j]].append(pl2[j])
            d[pl2[j]].append(pl1[j])

print(matches(["1 команда", "2 команда", "3 команда", "4 команда", "5 команда", "6 команда"]))

def matches(players):
    d = dict()
    pl1 = players[0:len(players)//2]
    pl2 = players[len(players)//2:]
    for i in range(len(pl1) * 2):
        print(i + 1, "тур:")
        # pl2.insert(0, pl2[-1])
        # pl2.pop(-1)

        pl1.insert(1, pl2[-1])
        pl2.insert(0, pl1[-1])
        pl2.pop(-1)
        pl1.pop(-1)
        for j in range(len(pl1)):
            print(pl1[j], "играет с", pl2[j])
        print('                                     ')


print(matches(["1 команда", "2 команда", "3 команда", "4 команда", "5 команда", "6 команда"]))

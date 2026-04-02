def matches(players):
    """
    This is program that conducts a draw with commands and returns dict with rounds and matches in this round
    :param players: str
    :return: dict
    """
    d = dict()
    pl1 = players[0:len(players)//2]
    pl2 = players[len(players)//2:]
    for i in range(len(pl1) * 2 - 1):
        pl1.insert(1, pl2[0]), pl2.append(pl1[-1])
        pl2.pop(0)
        pl1.pop(-1)
        d[str(i + 1) + " round:"] = []
        for x in range(len(pl1)):
            d[str(i + 1) + " round:"].append((pl1[x], pl2[x]))
    return d


print(matches(["1 command", "2 command", "3 command", "4 command", "5 command", "6 command"]))

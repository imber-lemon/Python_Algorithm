import random as rd

def matches(players):
    d = dict()
    for i in range(0, len(players)):
        if players[i] not in d:
            d[players[i]] = []
        op = rd.choice(players[i+1:])
        if op not in d[players[i]]:
            d[players[i]].append(op)
            if op not in d:
                d[op] = []
            d[op].append(players[i])
            print(d)
    #return d
print(matches(["George Floyd", "Charlie Kirk", "Jeffrey Epstein", "P Diddy"]))
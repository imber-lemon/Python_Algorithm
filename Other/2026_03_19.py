# import random as rd
#
#
# def matches(players):
#     d = dict()
#     for i in players:
#         op = rd.choice(players.remove(i))
#         if i not in d:
#             d[i] = []
#         if op not in d:
#             d[op] = []
#         if op in d[i] or players[i] == op:
#             op = rd.choice(players)
#         else:
#             d[i].append(op)
#             d[op].append(players[i])
#             print(d)
#     # return d

def matches(players):
    d = dict()
    for i in range(0, len(players)):
        d[players[i]] = players.remove(players[i])
    print(d)
print(matches(["1 команда", "2 команда", "3 команда"]))

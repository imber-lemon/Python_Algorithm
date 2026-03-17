def hIndex(citations):
    h = 0
    citations.sort(reverse=True)
    print(citations)
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            h = i + 1
    return h
print(hIndex([3, 0, 6, 1, 5]))


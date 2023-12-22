def second(k):
    return k[1]
S = [(3, 5), (2, 1), (5, 3), (1, 4), (4, 2)]
print(sorted(S, key = second, reverse=True))
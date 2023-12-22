S = [(3, 5), (2, 1), (5, 3), (1, 4), (4, 2)]
print(sorted(S, key = lambda k : k[0]))
print(sorted(S, key = lambda k : k[1], reverse=True))
print(sorted(S, key = lambda k : (k[0], k[1])))
print(sorted(S, key = lambda k : (k[0], -k[1]))) # First element will sort ascending order while second element sort in decending order
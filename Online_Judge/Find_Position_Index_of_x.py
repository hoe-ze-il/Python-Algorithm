import random

def seqsearch(x, S):
    for i in range(len(S)):
        if x == S[i]:
            return i
    return -1
def solve(S, X):
    for i in range(len(X)):
        print(seqsearch(X[i], S), end = " ")
    print()

SEED, MIN, MAX, N = list(map(int, input().split()))

random.seed(SEED)

S = random.sample(range(MIN, MAX), N)
X = random.sample(range(MIN, MAX), N)
solve(S, X)
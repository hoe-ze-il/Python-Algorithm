import random

def binsearch(n, S):
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2
        if S[mid] <= 0:
            low = mid + 1
        else:
            return S[mid]

    return 0

SEED, N = map(int, input().split())
random.seed(SEED)
S = sorted(random.sample(range(-10 * N, 10 * N), N))

print(binsearch(N, S))

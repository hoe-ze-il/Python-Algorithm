import random

def binsearch(x, n, S):
    low, high = 0, n - 1
    cnt = 0
    while low <= high:
        mid = (low + high) // 2
        cnt += 1
        if S[mid] == x:
            return cnt
        elif S[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return cnt

def solve(n, S, X):
    total = 0
    for i in range(n):
        total += binsearch(X[i], n, S)
    return total
        

SEED, MIN, MAX, N=2022,10,30,10
random.seed(SEED)
S=sorted(random.sample(range(MIN, MAX), N))
X=random.sample(range(MIN, MAX), N)

print(solve(N, S, X))
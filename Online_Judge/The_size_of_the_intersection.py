import random
def binsearch(x, n, S):
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if S[mid] == x:
            return mid
        elif S[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def solve(n, S, X):
    size = 0
    for i in range(n):
        j = binsearch(X[i], n, S)
        if j != -1:
            size += 1
    return size
        

SEED, MIN, MAX, N=2022,10,30,10
random.seed(SEED)
S=sorted(random.sample(range(MIN, MAX), N))
X=random.sample(range(MIN, MAX), N)

print(solve(N, S, X))
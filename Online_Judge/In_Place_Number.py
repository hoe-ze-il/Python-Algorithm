import random
def binsearch(n, S):
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if S[mid] == mid:
            return mid
        elif S[mid] < mid:
            low = mid + 1
        else:
            high = mid - 1
    return -1
SEED, N=12345, 5001
random.seed(SEED)
S=sorted(random.sample(range(-N,2*N,2), N))
print(binsearch(N, S))
def binsearch(n, s):
    low, high = 0, n - 1
    while low < high:
        mid = (low + high) // 2
        if s[mid] % 2 == 0:
            high = mid
        else:
            low = mid + 1
    if s[low] % 2 != 0:
        return -1
    return low

def solve(n, s):
    j = binsearch(n, s)
    print(0 if j < 0 else s[j])

N = int(input())
S = list(map(int, input().split()))
solve(N, S)
def binsearch(low, high, n, s):
    if low == high:
        if s[low] % 2 != 0:
            return -1
        else:
            return low
    else:
        mid = (low + high) // 2
        if s[mid] % 2 == 0:
            return binsearch(low, mid, n, s)
        else:
            return binsearch(mid + 1, high, n, s)
def solve(n, s):
    j = binsearch(0, n - 1, n, s)
    print(0 if j < 0 else s[j])
    

N = int(input())
S = list(map(int, input().split()))
solve(N, S)
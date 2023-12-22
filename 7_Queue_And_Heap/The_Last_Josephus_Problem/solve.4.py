def solve(n, k):
    f = 1
    for i in range(1, n + 1):
        f = ((f + k - 1) % i) + 1
    return f
N, K = map(int, input().split())
print(solve(N, K))
def solve(n, m):
    if 1 <= n <= m <= 2**64:
        return (m * (m + 1) // 2) - ((n - 1)* n // 2)
N, M = map(int, input().split())
print(solve(N, M))
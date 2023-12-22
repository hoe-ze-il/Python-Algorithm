def solve(A, B, M):
    r = A
    for _ in range(B - 1):
        r = r * A
    return r % M
A, B, M = map(int, input().split())
print(solve(A, B, M))
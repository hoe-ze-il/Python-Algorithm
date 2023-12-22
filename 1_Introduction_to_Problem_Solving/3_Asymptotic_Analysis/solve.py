def solve(N, S):
    maxn, maxi = S[0], 0
    for i in range(1, N):
        if maxn < S[i]:
            maxn, maxi = S[i], i
    return maxn, maxi
N = int(input())
S = list(map(int, input().split()))
maxn, maxi = solve(N, S)
print(maxn, maxi)
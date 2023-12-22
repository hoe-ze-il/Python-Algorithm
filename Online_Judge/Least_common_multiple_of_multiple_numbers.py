def gcd(n, m):
    while m != 0:
        n, m = m, n % m
    return n
def lcm(N, M):
    return N * M / gcd(N, M)
def LCM(x):
    result = x[0]
    for i in range(1, len(x)):
        result = lcm(result, x[i])
    return int(result)

X = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(f"{LCM(X)}\n")
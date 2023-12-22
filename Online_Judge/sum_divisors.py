def solve(n):
    s = 0
    i = 1
    if 1 <= n <= 2 ** 64:
        while i * i <= n:
            if n % i == 0:
                s += i
                if i != n // i:
                    s += n // i
            i += 1
    return s

N = int(input())
print(solve(N))

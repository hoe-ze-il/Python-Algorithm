def triple_fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    else:
        a, b, c = 1, 2, 3
        for _ in range(4, n + 1):
            a, b, c = b, c, (a + b + c)%(2**32 - 1)
        return c
N = int(input())
print(triple_fibonacci(N))
def result(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

N = int(input())
print(result(N))
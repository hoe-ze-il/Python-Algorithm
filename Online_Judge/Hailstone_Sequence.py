def collatz_largest(N, largest=0):
    if N == 1:
        return largest
    if N % 2 == 0:
        return collatz_largest(N // 2, max(largest, N))
    else:
        return collatz_largest(3 * N + 1, max(largest, N))


N = int(input())
print(collatz_largest(N))

def find_primes(n):
    sieve = [0, 0] + [1] * (n - 1)
    erased = []
    for i in range(2, int(n**0.5) + 1):
        if sieve[i] == 1:
            for j in range(i*i, n + 1, i):
                if sieve[j] == 1:
                    erased.append(j)
                sieve[j] = 0
    return erased


N, K = map(int, input().split())
erased_numbers = find_primes(N)

if K <= len(erased_numbers):
    print(erased_numbers[K - 1])
else:
    print(0)
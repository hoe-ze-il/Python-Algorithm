def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0], primes[1] = False, False

    for num in range(2, int(limit**0.5) + 1):
        if primes[num]:
            for multiple in range(num * num, limit + 1, num):
                primes[multiple] = False

    return [num for num in range(limit + 1) if primes[num]]

def find_twin_primes(primes):
    twin_primes = []
    for i in range(len(primes) - 1):
        if primes[i + 1] - primes[i] == 2:
            twin_primes.append((primes[i + 1], primes[i]))

    return twin_primes

primes_up_to_100 = sieve_of_eratosthenes(100)

twin_prime_pairs = find_twin_primes(primes_up_to_100)
for pair in twin_prime_pairs:
    print(pair[0], pair[1])

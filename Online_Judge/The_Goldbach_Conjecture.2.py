def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_sum_to_n(n):
    primes = [i for i in range(2, n) if is_prime(i)]
    result = []
    for prime in primes:
        complement = n - prime
        if complement in primes and complement >= prime:
            result.append((prime, complement))
    return result


n = int(input("Enter an even number N (2≤N≤30,000): "))
results = find_primes_sum_to_n(n)
for pair in results:
    print(pair[0], pair[1])
print(len(results))


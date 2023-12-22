def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_largest_primes(N, M):
    largest_primes = []
    num = M
    while len(largest_primes) < 5 and num >= N:
        if is_prime(num):
            largest_primes.append(num)
        num -= 1
    
    largest_primes.reverse()
    
    for prime in largest_primes:
        decimal_part = prime % 1.0
        if decimal_part < 0.5:
            print(f"{int(prime)}")
        else:
            print(f"{prime:.1f}")

N, M = map(int, input().split(" "))

find_largest_primes(N, M)

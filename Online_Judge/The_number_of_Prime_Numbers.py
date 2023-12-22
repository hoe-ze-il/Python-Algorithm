import random

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


SEED, MIN, MAX, N = map(int, input().split())
random.seed(SEED)
S = random.sample(range(MIN, MAX), N)

prime_count = sum(1 for num in S if is_prime(num))

print(prime_count)
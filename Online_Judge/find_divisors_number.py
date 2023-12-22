def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def is_divisors(n):
    if not is_prime(n):
        for i in range(1, n + 1):
            if n % i == 0:
                print(i)
n = int(input())
is_divisors(n)
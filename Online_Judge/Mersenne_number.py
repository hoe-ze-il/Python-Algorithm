import math
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def mersenne_prime(n):
    for i in range(2, int(math.log2(n + 1)) + 1):
        if is_prime(i):
            num = 2 ** i - 1
            if is_prime(num):
                print(num)
N = int(input())
mersenne_prime(N)

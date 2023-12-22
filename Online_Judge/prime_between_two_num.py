def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def prime_num(n, m):
    for i in range(n, m + 1):
        if is_prime(i):
            print(i)
N, M = map(int, input().split(" "))
prime_num(N, M)
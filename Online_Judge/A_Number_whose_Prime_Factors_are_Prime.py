def factorize(n):
    if n < 2:
        return []
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return [i] + factorize(n // i)
        return [n]
def count_prime_fact(nums):
    count = len(nums)
    return count

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
    
def solve(N, M):
    count = 0
    for i in range(N, M + 1):
        if is_prime(count_prime_fact(factorize(i))):
            count += 1
    return count

N, M = map(int, input().split())
print(solve(N, M))
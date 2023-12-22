def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def is_palindrome(n):
    s = str(n)
    r = s[::-1]
    return s == r
def solve(n, m):
    cnt = 0
    for i in range(n, m + 1):
        if is_prime(i) and is_palindrome(i):
            cnt += 1
    return cnt

N, M = map(int, input().split())
import time
start = time.time()
print(solve(N, M))
end = time.time()
print(end - start)
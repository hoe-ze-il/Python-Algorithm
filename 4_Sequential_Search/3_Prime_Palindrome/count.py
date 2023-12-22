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
    cnt1 = 0
    for i in range(n, m + 1):
        if is_prime(i):
            cnt1 += 1
    cnt2 = 0
    for i in range(n, m + 1):
        if is_palindrome(i):
            cnt2 += 1
    return cnt1, cnt2

N, M = map(int, input().split())
print(solve(N, M))
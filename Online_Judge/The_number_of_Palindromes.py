def is_palindrome(num):
    return str(num) == str(num)[::-1]

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solve(n, m):
    count = 0
    for num in range(n, m + 1):
        if is_palindrome(num):
            digit_sum = sum(int(i) for i in str(num))
            if is_prime(digit_sum):
                count += 1
    return count
N, M = map(int, input().split())
print(solve(N, M))
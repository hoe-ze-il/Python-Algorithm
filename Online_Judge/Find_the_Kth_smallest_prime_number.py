def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def kth(a, b, k):
    s = 0
    count = 0
    for i in range(a, b + 1):
        if is_prime(i):
            s += i
            count += 1
            if count == k:
                k = i
    print(s)
    print(k)

A, B, K = map(int, input().split(" "))
kth(A, B, K)

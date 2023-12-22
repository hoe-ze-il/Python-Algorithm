def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_natural(n):
    for i in n:
        if is_prime(i):
            print(f'{i} is a prime number.\n')
        else:
            print(f'{i} is a composite number.\n')

lst = []
for _ in range(5):
    n = int(input())
    lst.append(n)
is_natural(lst)
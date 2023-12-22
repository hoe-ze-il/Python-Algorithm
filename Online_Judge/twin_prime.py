def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def twin_prime(num):
    prime_num = []
    twin_prime_num = []
    count = 0
    for i in range(1, num + 1):
        if is_prime(i):
            prime_num.append(i)
    for i in prime_num:
        for j in prime_num:
            if j - i == 2:
                twin_prime_num.append([i, j])
                count += 1
    for i, j in twin_prime_num:
        print(i, j)
    print(count)

twin_prime(10)


def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0], primes[1] = False, False
    for num in range(2, int(limit**0.5) + 1):
        if primes[num]:
            for multiple in range(num * num, limit + 1, num):
                primes[multiple] = False
    return [num for num in range(limit + 1) if primes[num]]

def count_goldbach_triangles(odd_numbers, prime_list):
    cnt = 0
    for a in range(1, odd_numbers - 1):
        if a in prime_list:
            for b in range(a, odd_numbers - 1):
                if b in prime_list:
                    c = odd_numbers - a - b
                    if c in prime_list:
                        if b <= c and a + b > c:
                            cnt += 1
    return cnt

def solve(odd_numbers, prime_lst):
    for i in odd_numbers:
        print(count_goldbach_triangles(i, prime_lst), end = " ")

odd_numbers = list(map(int, input().split()))
primes_up_to_10000 = sieve_of_eratosthenes(10000)
solve(odd_numbers[1:], primes_up_to_10000)

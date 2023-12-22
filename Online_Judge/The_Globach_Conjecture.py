# Function to generate a list of prime numbers using the Sieve of Eratosthenes
def sieve_of_eratosthenes_primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    primes = []

    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                is_prime[i] = False

    return primes

# Function to count the number of Goldbach triangles that can be created
def count_goldbach_triangles(M, primes):
    count = 0
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            for k in range(j, len(primes)):
                if primes[i] + primes[j] + primes[k] == M:
                    count += 1
    return count

# Input
N = int(input())
odd_numbers = list(map(int, input().split()))

# Find the maximum odd number in the list
max_odd = max(odd_numbers)

# Generate a list of prime numbers up to the maximum odd number
primes = sieve_of_eratosthenes_primes(max_odd)

# Count the number of Goldbach triangles for each odd number and print the results
for odd_number in odd_numbers:
    if odd_number <= 5:
        print(0)
    else:
        count = count_goldbach_triangles(odd_number, primes)
        print(count)

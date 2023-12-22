# Which of the following numbers is a prime number?
# Select all the correct answers.
# 6, 5, 27, 54, 69, 95, 97

# My solution
def prime(N):
    result = ''
    if N <= 1:
        print('No')
    else:
        for i in range(2, N):
            if N % i == 0:
                result = 'Not a prime number'
                break
            else:
                result = f'{N} is a prime number'
    return result
N = int(input())
print(prime(N))
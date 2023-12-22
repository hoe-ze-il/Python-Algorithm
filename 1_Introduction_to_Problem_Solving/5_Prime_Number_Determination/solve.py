# Solution 1
# def solve(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# N = int(input())
# print('YES' if solve(N) else 'NO')

# ------------------------------------------

# Analyzing Performance
# def solve(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# N = int(input())
# import time

# start = time.time()

# print('YES' if solve(N) else 'NO')  

# end = time.time()

# print(f'solve() elapsed time: {end - start}')

# ------------------------------------------

#Solution 2
# def solve(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# N = int(input())
# print('YES' if solve(N) else 'NO')

# ------------------------------------------

#Analyzing Performance
def solve(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

N = int(input())
import time

start = time.time()
print('YES' if solve(N) else 'NO')
end = time.time()
print(f'solve() elapsed time: {end - start}')
# Solution 1
# def solve(n):
#     cnt = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             cnt += 1
#     return cnt
# N = int(input())
# print(solve(N))

#-------------------------------------

# Analyzing Performance 1
# def solve(n):
#     cnt = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             cnt += 1
#     return cnt
# N = int(input())
# import time

# start = time.time()

# print(solve(N))

# end = time.time()

# print(f'solve() elapsed time: {end - start}')

#-------------------------------------

# Solution 2
# def solve(n):
#     cnt = 0
#     sqrtn = int(n ** 0.5)
#     for i in range(1, sqrtn + 1):
#         if n % i == 0:
#             cnt += 2
#     if sqrtn* sqrtn == n:
#         cnt -= 1
#     return cnt
# N = int(input())
# print(solve(N))

#-------------------------------------

#  Analyzing Performace 2
def solve(n):
    cnt = 0
    sqrtn = int(n ** 0.5)
    for i in range(1, sqrtn + 1):
        if n % i == 0:
            cnt += 2
    if sqrtn* sqrtn == n:
        cnt -= 1
    return cnt
N = int(input())
import time

start = time.time()

print(solve(N))

end = time.time()

print(f'solve() eslapsed time: {end - start}')
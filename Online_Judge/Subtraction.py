def solve(n):
    reversed_n = n[::-1]
    return abs(int(reversed_n) - int(n))

N = input()
print(solve(N))
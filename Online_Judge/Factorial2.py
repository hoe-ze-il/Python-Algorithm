def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
def factorial_process(n):
    if n == 1:
        return 1
    else:
        return f"{n}*{factorial_process(n - 1)}"
N = int(input())
result = factorial_process(N)
print(f"{N}!=({result[::-1]})={factorial(N)}")
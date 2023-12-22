def factorial(n):
    if n == 1:
        return 1
    else:
        return f"{n}*{factorial(n - 1)}"
result = factorial(4)
print(result[::-1])
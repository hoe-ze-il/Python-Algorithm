def print_numbers(n):
    if n == 0:
        print(0)
    else:
        print_numbers(n - 1)
        print(n)

n = int(input())
print_numbers(n)

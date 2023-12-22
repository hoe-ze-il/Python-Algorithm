def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        print(f"{i}! = {factorial}")

n = int(input("Enter a positive integer: "))
calculate_factorial(n)
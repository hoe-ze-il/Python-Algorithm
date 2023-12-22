def sum_odd_pyramid(n):
    return (n * (n + 1) // 2) ** 2
N = int(input())
print(sum_odd_pyramid(N))
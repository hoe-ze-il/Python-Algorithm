def sum_of_nines(A, B):
    total_sum = 0
    for num in range(A, B + 1):
        if num % 10 == 9:
            total_sum += num
    return total_sum

A, B = map(int, input().split())

print(sum_of_nines(A, B))
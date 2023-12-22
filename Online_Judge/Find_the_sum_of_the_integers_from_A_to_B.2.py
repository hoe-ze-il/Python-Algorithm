def sum_of_fives(A, B):
    total_sum = 0
    for num in range(A, B + 1):
        tens_digit = (num // 10) % 10
        if tens_digit == 5:
            total_sum += num
    return total_sum

A, B = map(int, input().split())

result = sum_of_fives(A, B)
print(result)

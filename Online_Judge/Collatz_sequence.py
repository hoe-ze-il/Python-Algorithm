def collatz_sequence_length(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1
    return length

N, M = map(int, input().split())
max_length = 0
number_with_longest_sequence = 0

for i in range(N, M + 1):
    length = collatz_sequence_length(i)
    if length >= max_length:
        max_length = length
        number_with_longest_sequence = i

print(number_with_longest_sequence)
print(max_length)

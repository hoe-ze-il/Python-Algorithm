def collatz_sequence_operations(N):
    operations = 0
    
    while N > 1:
        if N % 2 == 0:
            N = N // 2
        else:
            N = (N + 1) // 2
        operations += 1
    
    return operations

N = int(input())

result = collatz_sequence_operations(N)
print(result)
def result(n):
    if n == 1:
        print(1)
        return 1
    else:
        print(n, end=" ")
        return result(n - 1)
        
N = int(input())
result(N)
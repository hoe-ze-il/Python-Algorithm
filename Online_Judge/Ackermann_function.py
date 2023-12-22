def A(n, m, call_count=0):
    if n == 0:
        call_count += 1
        return m + 1, call_count
    elif n > 0 and m == 0:
        call_count += 1
        result, call_count = A(n - 1, 1, call_count)
        return result, call_count
    elif n > 0 and m > 0:
        call_count += 1
        result1, call_count = A(n, m - 1, call_count)
        result2, call_count = A(n - 1, result1, call_count)
        return result2, call_count

n, m = map(int, input().split())
result, call_count = A(n, m)
print(result)
print(call_count)

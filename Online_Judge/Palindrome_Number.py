def is_palindrome(n):
    palindrome = str(n)[::-1]
    if int(palindrome) == n:
        return True
    return False

def solve(A, B):
    cnt = 0
    print(A, B)
    for i in range(A, B + 1):
        if is_palindrome(i):
            print(i, end=" ")
            cnt += 1
    print()
    return cnt

A, B = map(int, input().split())
print(solve(A, B))

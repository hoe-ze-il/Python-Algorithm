def solve(A, B):
    A_reverse = int(A[::-1])
    B_reverse = int(B[::-1])

    max_reversed = max(A_reverse, B_reverse)

    return max_reversed

A, B = input().split()

print(solve(A, B))
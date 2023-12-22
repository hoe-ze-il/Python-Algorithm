def is_allocation_possible(S, M, U):
    allocated_budget = 0
    for budget in S:
        allocated_budget += min(budget, U)
    
    return allocated_budget <= M

def solve(S, M):
    left, right = 0, max(S) 
    while left < right:
        mid = (left + right + 1) // 2 
        if is_allocation_possible(S, M, mid):
            left = mid
        else:
            right = mid - 1
    
    return left

N, M = map(int, input().split())
S = list(map(int, input().split()))

print(solve(S, M))
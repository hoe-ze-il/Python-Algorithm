from collections import deque

def solve(n, k):
    queue = deque([i for i in range(1, n + 1)])
    j = 0
    while len(queue) > 1:
        j = (j + k - 1) % len(queue)
        queue.rotate(-j)  # Use rotate instead of pop
        queue.popleft()   # Use popleft to remove the first element
        j = 0             # Reset j after rotation
    return queue[0]

N, K = map(int, input().split())
print(solve(N, K))
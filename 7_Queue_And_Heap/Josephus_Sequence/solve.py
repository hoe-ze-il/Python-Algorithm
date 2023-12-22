from collections import deque

def solve(n, k):
    queue = deque([i for i in range(1, n + 1)])
    while queue:
        for j in range(1, k + 1):
            if j != k:
              queue.append(queue.popleft())
            else:
                queue.popleft()
    return queue[0]

N, K = map(int, input().split())
print(solve(N, K))

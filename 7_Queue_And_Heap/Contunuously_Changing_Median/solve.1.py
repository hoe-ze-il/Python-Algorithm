from heapq import heappush, heappop

def solve(A):
    maxheap, minheap = [], []
    for a in A:
        heappush(maxheap, -a)
        heappush(minheap, -heappop(maxheap))
        if len(maxheap) < len(minheap):
          heappush(maxheap, -heappop(minheap))
        print(-maxheap[0], end = " ")
    print()
A = list(map(int, input().split()))
solve(A)
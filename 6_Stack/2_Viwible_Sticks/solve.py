from stack import Stack

def solve(n, s):
    stack = Stack()
    for i in range(n):
        while not stack.empty() and s[i] >= stack.peek():
            stack.pop()
        stack.push(s[i])
    return stack.size()

N = int(input())
S = list(map(int, input().split()))
print(solve(N, S))
def solve(S):
    open = "[{("
    close = "]})"
    stack = []

    for s in S:
        if s in open:
            stack.append(s)
        elif stack and open.index(stack[-1]) == close.index(s):
            stack.pop()
        else:
            return False
    return len(stack) == 0

S = input()
print("Yes" if solve(S) else "No")
def solve(n, c):
    lower = []
    upper = []
    for i in range(n):
        if c[i].islower():
            lower.append(c[i])
        else:
            upper.append(c[i])
    upper.sort()
    lower.sort(reverse=True)
    print("".join(map(str, upper)), end="  ")
    print("".join(map(str, lower)))
N = input().split()
n = int(N[0])
c = "".join(N[1:])
solve(n, c)
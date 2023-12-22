N = [int(i) for i in input().split()]
for i in range(4):
    mid = (len(N) - 1) // 2
    temp = N.pop(N[int(mid)])
print(temp)
def solve(data):
    sorted_data = sorted(data)
    for i in sorted_data:
        print(i, end = " ")

N = int(input())
data = list(map(int, input().split()))
for i in data:
    print(i, end=" ")
print()
solve(data)

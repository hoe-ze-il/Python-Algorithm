from itertools import permutations
import string
import time

N = int(input())
S = string.ascii_uppercase[:N]
start = time.time()

for p in permutations(S):
    print("".join(p))

end = time.time()
print(end - start)

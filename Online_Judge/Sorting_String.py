import random
from string import ascii_lowercase

def generate(SEED, N, K):
    random.seed(SEED)
    S=[]
    for _ in range(N):
        length=random.randint(1, N-1)
        s=random.sample(ascii_lowercase, length)
        S.append("".join(s))
    return S[K - 1]
S, N, K = map(int, input().split())
print(generate(S, N, K))
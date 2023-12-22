import random
def generate(SEED, MIN, MAX, N, K):
    random.seed(SEED)
    return random.sample(range(MIN, MAX), N).pop(K - 1)

SEED, MIN, MAX, N, K = map(int, input().split())
print(generate(SEED, MIN, MAX, N, K))
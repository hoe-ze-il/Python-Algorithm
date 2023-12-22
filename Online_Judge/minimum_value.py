import random

def solve(seed, min_val, max_val, n):
    if 1 <= min_val < max_val <= 10000 and 1 <= n <= 1000:
        random.seed(seed)
        min_value = float('inf')
        min_index = None

        for i in range(n):
            random_num = random.randint(min_val, max_val)
            if random_num < min_value:
                min_value = random_num
                min_index = i

        return f'{min_value} {min_index}'

SEED, MIN, MAX, N = map(int, input().split())
print(solve(SEED, MIN, MAX, N))

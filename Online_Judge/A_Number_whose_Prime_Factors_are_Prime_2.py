import random

def generate(SEED, MIN, MAX, N):

random.seed(SEED)

return random.sample(range(MIN, MAX), N)

SEED, MIN, MAX, N=2022,10,100,15

S=generate(SEED, MIN, MAX, N)

print(S)

[78, 46, 66, 79, 49, 84, 17, 76, 98, 62, 97, 91, 50, 11, 65]
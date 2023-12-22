def coin(n):
    if n == 1:
        return 1
    else:
        coins = [0] * (n + 1)
        coins[1] = 1
        for i in range(2, n + 1):
            if i % 2 == 0:
                coins[i] = coins[i // 2]
            else:
                coins[i] = coins[i // 2] + coins[i // 2 + 1]
        return max(coins)
N = int(input())
print(coin(N))
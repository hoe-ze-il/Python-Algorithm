def hanoi(n, src, via, dst):
    if n == 1:
        print(f"{src} -> {dst}")
    else:
        hanoi(n - 1, src, dst, via)
        hanoi(1, src, via, dst)
        hanoi(n - 1, via, src, dst)

N = int(input())
hanoi(N, "A", "B", "C")
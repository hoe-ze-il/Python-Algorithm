def solve(X):
    k = []
    for x in X:
        if x.isdigit():
            k.append(int(x))
        else:
            b, a = k.pop(), k.pop()
            if x == "+":
                result = a + b
                k.append(result)
            elif x == "-":
                result = a - b
                k.append(result)
            elif x == "*":
                result = a * b
                k.append(result)
            else:
                result = a // b
                k.append(result)
    return k[-1]

X=input()
print(solve(X))

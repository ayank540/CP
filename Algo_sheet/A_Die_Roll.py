def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        return gcd(a - b, b)
    return gcd(a, b-a)


Y, W = map(int, input().split())
max_ = max(Y, W)
A = 7 - max_
B = 6
g = gcd(A, B)
print(f"{A//g}/{B//g}")
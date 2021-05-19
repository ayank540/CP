n = input()
s = list(map(int, input().split()))
hired = 0
crimes = 0
for i in s:
    if i > 0:
        hired += i
    else:
        if i < 0 and hired > 0:
            hired -= 1
        else:
            crimes += 1

print(crimes)
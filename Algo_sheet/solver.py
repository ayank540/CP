input()
s = list(map(int, input().split()))
count = 0
police = 0
for i in s:
    if i == -1 and police == 0:
        count += 1
    else:
        while police > 0:
            count -= 1
            police-=1
    if i > 0:
        police = i
print(count)
n = int(input())
l = list(map(int, input().split()))
i, s, d = 0, 0, 0
j = n-1
while i <= j:
    if l[i] >= l[j]:
        s += l[i]
        i+=1
    else:
        s += l[j]
        j -= 1
    if i <= j:
        if l[i] >= l[j]:
            d += l[i]
            i+=1
        else:
            d += l[j]
            j -= 1
print(s, d)
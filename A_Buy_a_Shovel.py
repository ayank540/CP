k, m = list(map(int, input().split()))
i = 1
while True:
    if(k * i) % 10 == m or (k * i) % 10 == 0:
        print(i)
        break
    i += 1

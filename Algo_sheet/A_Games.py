n = int(input())
home = []
guest = []
for i in range(n):
    temp = list(map(int, input().split()))
    home.append(temp[0])
    guest.append(temp[1])
ch = 0
for i in range(n):
    for j in range(n):
        if home[i] == guest[j]:
            ch+=1
print(ch)
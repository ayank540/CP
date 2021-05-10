l = list(map(int , input().split()))
l.sort()
c = 0
for i in range(3):
    if l[i] == l[i+1]:
        c+=1
print(c)
n = list(map(int, input().split()))
s = input()
cal = 0
for i in s:
    cal += n[int(i)-1]
print(cal)
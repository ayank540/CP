s = input()
c = 0
if s[0] <= 'a':
    x = ord('a') - ord(s[0])
    if x <= 13:
        c += x
    else:
        x += 26 - x
else:
    x = ord(s[0]) - ord('a')
    if x <= 13:
        c += x
    else:
        c += 26 - x
for i in range(len(s)-1):
    if s[i] <= s[i+1]:
        x = ord(s[i]) - ord(s[i+1]) + 26
        if x <= 13:
            c += x
        else:
            c += 26 - x
    else:
        x = ord(s[i+1]) - ord(s[i]) + 26
        if x <= 13:
            c += x
        else:
            c += 26 - x
print(c)

# Input: R|G|G|B|B|R|R|R|B
# Output: B|B|B|G|G|R|R|R|R

s = list(map(str, input().split()))
len_ = len(s)

########## APPROACH 1 ##########
# Using in-built sort or sorted function
for i in sorted(s):
    print(i, end=" ")

########## APPROACH 2 ##########
# Using counting sort
r = 0
g = 0
b = 0
for i in s:
    if 'R' == i:
        r += 1
    elif 'G' == i:
        g += 1
    elif 'B' == i:
        b += 1
i = 0
while b:
    s[i] = 'B'
    i+=1
    b-=1

while g:
    s[i] = 'G'
    i+=1
    g-=1

while r and i < len_:
    s[i] = 'R'
    i+=1
    g-=1

for i in s:
    print(i, end=" ")

# Now, interviewer says, solve it using only one pass and no auxiliary space
########## APPROACH 3 ##########
# r = len_
# b = -1
# i = 0
# while i < r:
#     if s[i] == 'B':
#         b += 1
#         s[i], s[b] = s[b], s[i]
#         i+=1
#     elif s[i] == 'R':
#         r -= 1
#         s[i], s[r] = s[r], s[i]
#         i+=1
#     elif s[i] == 'G': 
#         i+=1

# for i in s:
#     print(i, end=" ")

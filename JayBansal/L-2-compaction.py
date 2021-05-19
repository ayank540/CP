# Input: |0|3|2|5|0|0|1|2|0
# Output: |0|0|0|0|3|2|5|1|2

arr = list(map(int, input().split()))
nz = len(arr)
t = nz - 1
while t >= 0:
    if arr[t] != 0:
        nz -= 1
        temp = arr[t]
        arr[t] = arr[nz]
        arr[nz] = temp
    t -= 1

for i in range(len(arr)):
    print(arr[i], end=" ")

# arr = [3,2,5,-1,-5,-8,0,3]
arr = [-10, -2, -30, -40, -3, -1]

sum = 0
maxSum = float('-inf')
for i in arr:
    sum = max(i, sum+i)
    maxSum = max(maxSum, sum)
print(maxSum)

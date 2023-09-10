n = int(input())
nums = input().split()
numst = sum(range(1,n+1))
sum = 0
for i in range(n-1):
    sum += int(nums[i])

print(numst - sum)
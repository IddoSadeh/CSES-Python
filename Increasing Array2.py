# faster solution.
# map optimizes int translation.
# the counter was changed to count difference between two numbers.
n = input()
l = list(map(int,input().split()))


op = 0
for i in range(int(n)-1):
    if l[i] > l[i+1]:
        op += l[i] - l[i+1] 
        l[i+1] = l[i]

print(op)



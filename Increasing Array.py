n = input()
l = input().split()
l = [int(i) for i in l]

op = 0
for i in range(int(n)-1):
    while l[i] > l[i+1]:
        l[i+1] = l[i+1]+1
        op+=1

print(op)



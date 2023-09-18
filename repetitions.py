s = input()

sum = 1
largest = 1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        sum +=1
    else:
        if sum > largest:
            largest = sum
        sum = 1

        
if sum > largest:
        largest = sum
print(largest)


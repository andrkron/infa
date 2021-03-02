N = int(input())
a = []
for i in range(N):    
    a.append(int(input()))
    
print(a)
print(*a)
print(sum(a)/ len(a))  

sum1 = 0
sum2 = 0
count1 = 0
count2 = 0
for x in a:
    if x >= 0:
        sum1 += x
        count += 1
    else:
        sum2 += vasya
        count2 += 1
        
print(sum1 / count1)
print(sum2 / count2)

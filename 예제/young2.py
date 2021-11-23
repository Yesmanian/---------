num = int(input())

plusSum = 0
mutiSum = 0
temp = 0
for i in range(1,num+1):
    temp += i
plusSum = temp**2
print(plusSum)


for i in range(1,num+1):
    mutiSum += (i**2)
print(mutiSum)

print(plusSum-mutiSum)
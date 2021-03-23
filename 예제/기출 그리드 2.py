n = input()
array = list(n)
result = int(array[0])
print(result)
for i in range(1,len(array)):
    temp = int(array[i])
    if int(array[i-1]) == 0 or temp == 0:
        result+=temp
    else:
        result*=temp

print(result)

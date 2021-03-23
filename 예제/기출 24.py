n = int(input())
house = list(map(int,input().split()))

min = 100000
answer = 0
for i in house:
    count = 0
    for j in house:
        count += abs(i-j)
    if count < min:
        min = count
        answer = i
print(answer)
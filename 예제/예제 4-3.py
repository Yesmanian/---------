location = input()
xyLocation =[]
xyLocation.append(ord(location[0])-96)
xyLocation.append(int(location[1]))
print(xyLocation)

count = 0

dx = [2,-2,-2,-2]
dy = [1,-1,1,-1]

for i in range(4):
    xyLocation[0] += dx[i]
    xyLocation[1] += dy[i]
    if xyLocation[0] < 1 or xyLocation[0] > 8 or xyLocation[1] < 1 or xyLocation[1] > 8:
        continue
    count+=1
print(count)
temp = [[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,1,1,1,1],[1,0,0,0,1],[1,0,0,0,1]]
temp1 = [[1,0,0,0,1],[1,1,1,1,1],[1,0,0,0,1]]
map1 = []
cnt =1

def rotated(a):
  n = len(a)
  m = len(a[0])

  result = [[0]* n for _ in range(m)]

  for i in range(n):
    for j in range(m):
      result[j][n-i-1] = a[i][j]
  return result

# map2 = []
# for i in range(len(temp)):
#     if i == 0:
#         map1.append(temp[i])
#
#     elif temp[i] != map1[-1]:
#         map1.append(temp[i])


    #     cnt +=1
    # if temp[i] not in map1:
    #     map1.append(temp[i])
# map2 = rotated(map1)
# map3 = []
# for i in range(len(map2)):
#     if i == 0:
#         map3.append(map2[i])
#
#     elif map2[i] != map3[-1]:
#         map3.append(map2[i])

# print(map1)
# print(map2)
# print(map3)

def check(a):
    newMap = []
    for i in range(len(a)):
        if i == 0:
            newMap.append(a[i])

        elif a[i] != newMap[-1]:
            newMap.append(a[i])
    return newMap


def soulution(map):
    result = []
    while True:
        map1 = check(map)
        map2 = rotated(map1)
        map3 = check(map2)
        if rotated(rotated(rotated(map3))) == map1:
            break
    print(map3)

print(soulution(temp))






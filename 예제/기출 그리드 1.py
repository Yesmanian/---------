# from collections import deque
# n = int(input())
#
# array =list(map(int,input().split()))
# array.sort()
#
# result = 0
# count = 0
# for i in array:
#     count+=1
#     if count >=i:
#         result+=1
#         count=0
# print(result)

#2 잘못품
n = int(input())
array = list(map(int,input().split()))
print(array)
array.sort(reverse=True)
count = 0
for i in array:
    if len(array) >= i:
        count+=1
        for _ in range(i):
            array.pop(0)
print(count)
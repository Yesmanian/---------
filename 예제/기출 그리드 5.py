# n, m = map(int,input().split())
# array = list(map(int,input().split()))
# count = 0
# for i in range(0,n-1):
#     temp = array[i]
#     for j in array[i+1:]:
#         if temp != j:
#             count+=1
# print(count)

#2
n, m = map(int,input().split())
array = list(map(int,input().split()))
count = 0
for i in range(len(array)-1):
    for j in array[i+1:]:
        if array[i] != j:
            count +=1
print(count)
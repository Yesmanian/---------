# s = list(input())
# print(s)
# count=0
# for i in range(1,len(s)):
#     if s[i] != s[i-1]:
#         count+=1
# print(count//2)

#2
array = list(map(int,input()))
print(array)

count0 = 0
count1 = 0
for i in range(len(array)-1):
    temp = array[i]
    if temp == 0 and temp != array[i+1]:
        count0 +=1
    if temp == 1 and temp != array[i+1]:
        count1 +=1
if array[-1] != array[-2] and array[-1] == 0:
    count0+=11
if array[-1] != array[-2] and array[-1] == 1:
    count1+=1
print(min(count0,count1))
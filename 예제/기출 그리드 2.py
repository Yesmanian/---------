# n = input()
# array = list(n)
# result = int(array[0])
# print(result)
# for i in range(1,len(array)):
#     temp = int(array[i])
#     if int(array[i-1]) == 0 or temp == 0:
#         result+=temp
#     else:
#         result*=temp
#
# print(result)

#2
n = int(input())
array = list(input())
array = list(map(int,array))
print(array)
result = 0
for i in range(1,len(array)):
    if array[i-1] == 0 or array[i] == 0:
        result +=array[i-1]+array[i]
        print(result)
    else:
        if result == 0:
            result = array[i-1]
        result *=array[i]
        print(result)
print(result)

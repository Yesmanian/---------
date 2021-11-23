from itertools import combinations

array = [[0] * 2 for _ in range(2)]
print(array)

list1 = []
for i in range(2):
    for j in range(2):
        list1.append([i,j])
print(list1)
result = list(combinations(list1,2))
print(result)
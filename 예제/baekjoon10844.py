n = int(input())

cnt = 0

def dfs(x,L):
    global cnt
    if L == n-1:
        cnt +=1
        return
    if x == 0:
        dfs(x+1,L+1)
    elif x == 9:
        dfs(x-1,L+1)
    else:
        dfs(x+1,L+1)
        dfs(x-1,L+1)

# dfs(9,0)
# print(cnt)

for i in range(1,10):
    dfs(i,0)
print(cnt)
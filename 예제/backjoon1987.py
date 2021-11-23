R ,C = map(int,input().split())
alplist = [list(input()) for _ in range(R)]
print(R,C)
print(alplist)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
temp = [alplist[0][0]]
answer = 0


def bfs(x,y,temp):
    global answer
    answer = max(len(temp),answer)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        print(nx,ny)
        if  nx <= -1 or ny <= -1 or nx >= R or ny >= C:
            continue
        elif alplist[nx][ny] not in temp:

            temp.append(alplist[nx][ny])
            bfs(nx,ny,temp)
            temp.pop()



print(bfs(0,0,temp))
print(temp)
print(answer)
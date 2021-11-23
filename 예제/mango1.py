
n =4
horizontal = 'true'
# 상하좌우
directionX = [-1,1,0,0]
directionY = [0,0,-1,1]
global x
global y
x = 0
y = 0
def RDL(start,size,room):
    # R
    global x
    global y

    nx = x + directionX[3]
    ny = y + directionY[3]
    room[nx][ny] = room[x][y] + 1
    x = nx
    y = ny
    # D
    for _ in range(size):
        nx = x + directionX[1]
        ny = y + directionY[1]
        room[nx][ny] = room[x][y] + 1
        x = nx
        y = ny

    # L
    for _ in range(size):
        nx = x + directionX[2]
        ny = y + directionY[2]
        room[nx][ny] = room[x][y] + 1
        x = nx
        y = ny


    return room

def DRU(start,size,room):
    global x
    global y
    # D

    nx = x + directionX[1]
    ny = y + directionY[1]
    room[nx][ny] = room[x][y] + 1
    x = nx
    y = ny
    # R
    for _ in range(size):
        nx = x + directionX[3]
        ny = y + directionY[3]
        room[nx][ny] = room[x][y] + 1
        x = nx
        y = ny
    # U
    for _ in range(size):
        nx = x + directionX[0]
        ny = y + directionY[0]
        room[nx][ny] = room[x][y] + 1
        x = nx
        y = ny
    return room
def solution(n,horizontal):
    answer = [[]]

    start = 1
    room = [[0] * n for _ in range(n)]
    room[0][0] = start

    size = 1


    # if horizontal == 'true':

        # RDL(start,size,room)
        # size +=1
        #
        # DRU(start, size, room)
        #
        # size +=1
        # RDL(start, size, room)
    if horizontal == 'true':
        for i in range(n-1):
            if i % 2 == 0:
                RDL(start, size, room)
                size += 1
            else:
                DRU(start, size, room)
                size += 1
    else:
        for i in range(n-1):
            if i % 2 == 0:
                DRU(start, size, room)
                size += 1
            else:
                RDL(start, size, room)
                size += 1
    print(room)
    print(x,y)
        # 오른 아래 왼
        # 아래 오른 위
        # 오른 아래 왼

    # 아래 오른 위
    # 오른 아래 왼
    # 아래 오른 위








    return room

print(solution(n,horizontal))
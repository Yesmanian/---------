import sys
diceUp = [0,0]
diceFront = [0,0]
diceRight = [0,0]

mapp = []
N,M,x,y,k = map(int,sys.stdin.readline().rstrip().split())

for _ in range(N):
    mapp.append(list(map(int,sys.stdin.readline().rstrip().split())))

move = list(map(int,sys.stdin.readline().rstrip().split()))
# mapp = [[0,2],[3,4],[5,6],[7,8]]
# move = [4,4,4,1,3,3,3,2]

# print(mapp)
# print(move)

for i in move:

    # 동
    if i == 1 and x + 1 < M:
        x += 1
        if mapp[y][x] == 0:
            mapp[y][x] = diceRight[0]

        else:
            diceRight[0] = mapp[y][x]
            mapp[y][x] = 0

        diceUp, diceRight = diceRight,diceUp
        diceUp[0],diceUp[1] = diceUp[1],diceUp[0]
        print(diceUp[0])

    # 서
    if i == 2 and x - 1 >=   0:
        x -= 1
        if mapp[y][x] == 0:
            mapp[y][x] = diceRight[1]

        else:
            diceRight[1] = mapp[y][x]
            mapp[y][x] = 0

        diceUp, diceRight = diceRight, diceUp
        diceRight[0],diceRight[1] = diceRight[1],diceRight[0]
        print(diceUp[0])

    #  북
    if i == 3 and y - 1 >= 0:
        y -= 1
        if mapp[y][x] == 0:
            mapp[y][x] = diceFront[1]

        else:
            diceFront[1] = mapp[y][x]
            mapp[y][x] = 0

        diceUp, diceFront = diceFront, diceUp
        diceFront[0],diceFront[1] = diceFront[1],diceFront[0]
        print(diceUp[0])

    #  남
    if i == 4 and y + 1 < N:
        y += 1
        if mapp[y][x] == 0:
            mapp[y][x] = diceFront[0]

        else:
            diceFront[0] = mapp[y][x]
            mapp[y][x] = 0

        diceUp, diceFront = diceFront, diceUp
        diceUp[0],diceUp[1] = diceUp[1],diceUp[0]
        print(diceUp[0])



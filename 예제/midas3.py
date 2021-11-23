N = 9
mine = [ [1, 1], [1, 7], [2, 7], [3, 6], [4, 1], [4, 4], [4, 8], [8, 4], [8, 5], [9, 6] ]


def solution(N, mine):

    board = [ [0] * (N+2) for _ in range(N+2)]


    for i in mine:
        board[i[0]][i[1]] = -1



    for i in range(1,N+1):
        for j in range(1,N+1):
            if board[i][j] == 0:
                count = 0
                for k in range(i-1,i+2):
                    for m in range(j-1,j+2):
                        if board[k][m] == -1:
                            count+=1
                board[i][j] = count



    print(board)
    answer = []

    del board[0]
    del board[N]
    print(board)

    for i in board:
        del i[0]
        del i[N]
        answer.append(i)

    return answer

print(solution(N,mine))

rows = 3
columns = 3
def solution(rows, columns):
    answer = [[]]

    map = [[0] * columns for _ in range(rows)]
    print(map)

    number = 1
    x = 0
    y = 0
    map[0][0] = number
    zeroCnt = rows * columns -1

    # all 0 // 더이상 안바뀌는거

    while zeroCnt != 0:

        number += 1

        if map[y][x] % 2 == 0:

            if (y+1) == rows:
                y = 0
            else:
                y += 1

            if x == 0 and y == 0 and map[y][x] % 2 == 1:
                break

            if map[y][x] == 0:
                zeroCnt -= 1
                map[y][x] = number
            if zeroCnt == 0:
                break
            else:
                map[y][x] = number
        else:
            if (x + 1) == columns:
                x = 0
            else:
                x = x + 1


            if map[y][x] == 0:
                zeroCnt -= 1
                map[y][x] = number
            if zeroCnt == 0:
                break
            else:
                map[y][x] = number

        print(map)






    print(map)
    return answer

print(solution(rows,columns))
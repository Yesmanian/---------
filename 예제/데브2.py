
rows = 6
columns = 6
queries = 	[[2,2,5,4],[3,3,6,6],[5,1,6,3]]

def solution(rows, columns, queries):
    table = []
    count = 1
    for i in range(rows):
        temp = []
        for j in range(columns):
            temp.append(count)
            count += 1
        table.append(temp)
    print(table)

    for i in queries:
        x1,y1,x2,y2 = i[0],i[1],i[2],i[3]
        temp = []
        ans = []
        for k in range(y1,y2+1):
            ans.append(table[x1][k])
            if k == y1:
                table[x1][k] = table[x1+1][k]
            else:
                table[x1][k] = ans[len(ans)-1]
        for k in range(x1+1,x2+1):
            ans.append(table[k][y2])
            table[k][y2] = ans[len(ans)-1]
        for k in range(y2,y1-1,-1):
            ans.append(table[x2][k])
            print(k)
        print(ans)
        # for x in range(x1,x2+1):
        #     for y in range(y1,y2+1):
        #
        #         ans.append(table[x][y])
        #         if x == x1:
        #             if y == y1:
        #
        #                 table[x][y] = table[x+1][y]
        #
        #             else:
        #                 table[x][y] = ans[len(ans)-1]
        #         if y == y2:
        #             if x == x1:
        #
        #                 table[x][y] = taa
        #
        #         temp.append((x,y))
        #
        #
        # print(temp)


    array = []


    answer = []
    return answer

print(solution(rows,columns,queries))
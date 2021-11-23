N =6
K =4
T =	[ [1,3],[3,4],[2,4],[2,4],[2,3],[1,2] ]


def solution(N,K,T):

    day = [0] * ( K + 1 )
    T.sort(key = lambda x: (int(x[0]),int(x[1])))
    print(T)

    for i in T:
        min = i[0]
        if  day[min] == 0:
            day[min] = 1

        elif day[min] == 1 :
            day[min+1] = 1
    print(day)



    answer = day.count(1)




    return answer

solution(N,K,T)
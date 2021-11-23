
play_list =[2, 3, 1, 4]

listen_time = 3



def solution(play_list, listen_time):

    temp = []
    temp2 = []
    count = 1
    for i in play_list:
        if i != 1:
            temp.append([count,i+count-1])
        else:
            temp.append([count,i+count])
        count += i
    print(temp)
    total = sum(play_list)
    for i in temp:
        temp2.append([i[0]+total,i[1]+total])

    print(temp2)

    for i in temp2:
        temp.append(i)

    print(temp)

    max = 0
    for i in range(1,total*2 - listen_time):
        answer = 0
        between = [i,i+listen_time]

        for k in between:
            for j in temp:
                a = j[0]
                b = j[1]
                if a<= k <=b:
                    answer+=1
        if answer >= max:
            max =  answer



    return max

solution(play_list,listen_time)
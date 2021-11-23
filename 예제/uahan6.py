time = 3.5
plans = [ ["홍콩", "11PM", "9AM"], ["엘에이", "3PM", "2PM"] ]

def solution(time, plans):
    answer = ''


    # for i in plans:
    #     if i[1][-2:] == 'PM':
    #         startTime = 12 + int(i[1][:-2])
    #         if startTime < 18:
    #             useTime = 18 - startTime
    #         if i[2][-2:] == 'AM':
    #
    #
    #         elif i[2][-2:] == 'PM':
    index = 0
    for i in plans:
        if i[1][-2:] == 'PM':
            plans[index][1] = 12 + int(i[1][:-2])
        else:
            plans[index][1] = int(i[1][:-2])
        if i[2][-2:] == 'AM':
            plans[index][2] = int(i[2][:-2])
        else:
            plans[index][2] = 12 + int(i[2][:-2])
        index += 1
    print(plans)

    for i in plans:
        useTime = 0
        # 9:30때

        if i[1] < 18:
            if i[1] <= 9:
                useTime = 8.5
            else:
                useTime = 18 - i[1]
        if i[2] > 13:
            if i[2] > 18:
                useTime += 5
            else:
                useTime += (i[2] - 13)
        print(useTime)
        if useTime <= time:
            time -= useTime
            answer = i[0]






    return answer

print(solution(time,plans))

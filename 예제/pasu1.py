
balloons = [[2,2],[4,4],[1,4],[-1,-4],[0,4],[0,3],[1,0],[-1,0],[-2,0],[-3,0]]



def solution(balloons):
    answer = 0

    giulPP = []
    giulMP = []
    giulMM = []
    giulPM = []
    temp = [giulPP,giulMP,giulMM,giulPM]

    for i in balloons:

        if i[0] >= 0 and i[1] > 0:
            print('PP')
            if i[0] == 0:
                giulPP.append(0)
            else:
                giulPP.append(i[1]/i[0])
        if i[0] < 0 and i[1] >= 0:
            print('MP')
            if i[1] == 0:
                giulMP.append(0)
            else:
                giulMP.append(i[1]/i[0])
        if i[0] <= 0 and i[1] < 0:
            print('MM')
            if i[0] == 0:
                giulMM.append(0)
            else:
                giulMM.append(i[1]/i[0])
        if i[0] > 0 and i[1] <= 0:
            print('PM')
            if i[1] == 0:
                giulPM.append(0)
            else:
                giulPM.append(i[1]/i[0])


    for i in temp:
        print(i)

    #     if i[1] > 0:
    #         giulP.append(i[1]/i[0])
    #     else:
    #         giulM.append(i[1]/i[0])
    # print(giulM)
    # print(giulP)

    answer = len(set(giulPP)) + len(set(giulMP)) +len(set(giulPM)) + len(set(giulMM))

    # for i in balloons:
    #     giul.append(i[0]/i[1])
    # print(giul)



    return answer

print(solution(balloons))
# a = [1,2,3]
# b = [2,1,3]
# if a == b:
#     print("aa")
# if a !=b:
#     print("asdf")

print(14/3)
print(28/6)

log = ["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"]

def solution(log):
    answer = ''

    startTime = []
    endTime = []
    for i in range(len(log)):
        if i % 2 == 0:
            startTime.append(log[i])
        else:
            endTime.append(log[i])
    print(startTime)
    print(endTime)

    studyTime = []
    for i in range(len(startTime)):

        studyTime.append((int(endTime[i][:2])*60 + int(endTime[i][-2:])) - (int(startTime[i][:2])*60 + int(startTime[i][-2:])))
    print(studyTime)

    realStudyTime = 0
    for i in studyTime:
        if i > 105:
            realStudyTime += 105
        elif i >= 5:
            realStudyTime += i

    print(realStudyTime)

    time = realStudyTime // 60
    if time < 10:
        answer += ("0" + str(time))
    else:
        answer += str(time)

    min = realStudyTime % 60
    if min < 10:
        answer += (":0" + str(min))
    else:
        answer += (":" + str(min))

    print(time,min)







    return answer

print(solution(log))
def hot_cold(emotion):
    # emotion 리스트 속에서 냉정과 열정 사이의 사랑의 개수를 세어 반환해 보세요.
    answer = 0

    feel = ""
    cnt = 0
    queue = []
    # for i in range(len(emotion)):
    #     if (emotion[i] == '냉정' or emotion[i] == '열정') and emotion[i] != feel:
    #         answer += cnt
    #         cnt = 0
    #         feel = emotion[i]
    #     # elif emotion[i] != feel and emotion[i] != '사랑':
    #     #     answer += cnt
    #     else:
    #         cnt +=1
    #     print(cnt)
    for i in emotion:
        if queue == [] and i != '사랑':
            queue.append(i)
            continue
        if queue[0] == i:
            queue = []
        if i == '사랑':
            queue.append(i)

        else:
            # queue.append(i)
            answer += (len(queue) - 1)
            queue = [i]






    return answer


# 3이 출력되어야 합니다.
print(hot_cold(['열정', '사랑', '사랑', '사랑', '냉정', '사랑', '사랑']))
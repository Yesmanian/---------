lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]


def solution(lottos, win_nums):
    answer = []
    count = 0
    count0 = lottos.count(0)

    for i in lottos:
        if i != 0 and i in win_nums:
            count += 1

    if count0 == 6:
        return [1, 6]

    answer.append((7 - count) - count0)
    answer.append(7 - count)
    return answer

print(solution(lottos,win_nums))
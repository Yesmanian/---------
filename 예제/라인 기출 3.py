enter = [1,4,2,3]
leave = [2,1,3,4]


def solution(enter, leave):
    answer = [0,0,0,0]
    inside = []
    for i in enter:
        inside.append(i)
        if leave[0] in inside:
            leave.pop(0)

            for j in inside:
                answer[j-1]+=(len(inside)-1)
            inside.pop()

    return answer

print(solution(enter,leave))
#2213
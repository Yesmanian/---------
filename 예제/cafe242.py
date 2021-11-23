

param =35

# 15
def solution(param):
    answer = 0

    for i in range(1,param):
        temp = list(str(i))

        for j in temp:
            if j == '3' or  j == '6' or j == '9':
                answer += 1

    return answer

print(solution(param))
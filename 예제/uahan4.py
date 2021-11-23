
# s ="aaabbaaa"
s ="wowwow"
def solution(s):
    answer = []

    diffIndex = 0
    for i in range(1,len(s)):

        if s[i] != s[0]:
            diffIndex = i
            break
    print(diffIndex)

    temp = s[diffIndex:]+s[:diffIndex]
    print(temp)

    cnt = 1
    for i in range(0,len(temp)-1):

        if temp[i+1] == temp[i]:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)
    answer = sorted(answer)

    return answer

print(solution(s))
number = 1231234
k = 3

def solution(number, k):
    answer = ''
    tempList = list(map(int,str(number)))
    print(tempList)
    a = []
    count = 0
    for i in tempList:
        a.append(i)
        if len(a) == k:
            maxValue = max(a)
            print(maxValue)
            print(a)
            for j in a:
                if j < maxValue:
                    a.remove(j)
                    count += 1
            print(a)
            for k in a:
                answer+=str(k)
            a = []
        print(answer)
    for k in a:
        answer+=str(k)


    return answer
print(solution(number,k))